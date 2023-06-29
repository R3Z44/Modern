from django import forms
from django.forms import ModelForm
from .models import Contact, Newsletter
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
