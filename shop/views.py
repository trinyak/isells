from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from shop.forms import WebsiteForm
from shop.models import Website
from django.contrib.auth.models import User
from shop.tasks import addWebsite

def create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            site = Website(
                name=form.cleaned_data['name'],
                slug=form.cleaned_data['slug'],
                domain = form.cleaned_data['slug'] + 'isells.eu',
                plan=form.cleaned_data['plan'],
                user=User.objects.get(pk=1)
            )

            site.save()
            addWebsite.delay(site)

            return HttpResponseRedirect('/shop/wait') # Redirect after POST
    else:
        form = WebsiteForm(initial={'plan': '2'}) # by default Standard

    return render_to_response('shop/website.html', {'form': form}, context_instance=RequestContext(request))

def wait(request):
    return render_to_response('shop/wait.html', {}, context_instance=RequestContext(request))