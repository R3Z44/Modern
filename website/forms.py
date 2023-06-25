from django import forms
from django.forms import ModelForm
from .models import Contact, Newsletter


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
