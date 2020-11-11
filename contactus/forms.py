from django import forms
from .models import ContactUS


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = '__all__'
