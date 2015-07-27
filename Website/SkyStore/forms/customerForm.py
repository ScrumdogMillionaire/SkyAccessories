__author__ = 'iri03'

from django.forms import ModelForm

from SkyStore.models.Customer import Customer

class Register(ModelForm):

    class Meta:
        model = Customer
        fields = ('email', 'password')