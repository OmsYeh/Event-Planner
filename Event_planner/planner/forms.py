from django import forms
from .models import *


class ResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceList
        fields = ['title', 'description']  # to use all fields of a model use __all__ in a string.


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = ['name', 'email']  # to use all fields of a model use __all__ in a string.


