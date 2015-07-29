__author__ = 'iri03'

from django.forms import ModelForm
from django import forms

class AddProductForm(forms.Form):
    productname = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    price = forms.CharField(max_length=8)
    quantity = forms.IntegerField()
    fileinput = forms.FileField()
