from django import forms
from django.forms import ModelForm
from web.models import ContactForm


class ContactFormModelForm(ModelForm):
    class Meta:
        model=ContactForm
        fields= ['customer_email', 'customer_name', 'message']