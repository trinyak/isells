from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from shop.forms import WebsiteForm
from shop.models import Website
from shop.tasks import addWebsite
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render_to_response('shop/index.html', {}, context_instance=RequestContext(request))


def create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            site = Website(
                name=form.cleaned_data['name'],
                slug=form.cleaned_data['slug'],
                plan=form.cleaned_data['plan'],
                user=request.user
            )
            site.save()

            # hack, need to find a better way
            site.domain = site.slug + '.isells.eu';
            site.save()

            addWebsite.delay(site)

            return HttpResponseRedirect('/shop/wait/' + str(site.pk)) # Redirect after POST
    else:
        form = WebsiteForm(initial={'plan': '2'}) # by default Standard

    return render_to_response('shop/create.html', {'form': form}, context_instance=RequestContext(request))


def wait(request, site_id):
    site = Website.objects.get(pk=site_id)
    return render_to_response('shop/wait.html', {'site': site}, context_instance=RequestContext(request))


def check_status(request, site_id):
    site = Website.objects.get(pk=site_id)

    if site.created:
        return HttpResponse()
    else:
        return HttpResponseNotFound()

