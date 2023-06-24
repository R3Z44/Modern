from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            new_contact.name = 'Unknown'
            new_contact.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your Message has been received successfully!!!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your Message didn\'t received!!!')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def services_view(request):
    return render(request, 'website/services.html')


def team_view(request):
    return render(request, 'website/team.html')
