from django import forms
from shop.models import Website

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name', 'slug', 'plan')
