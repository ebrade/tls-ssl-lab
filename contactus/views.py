from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

class ContactView():
    form = ContactForm()