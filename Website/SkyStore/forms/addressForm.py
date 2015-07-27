__author__ = 'iri03'

from django.forms import ModelForm

from SkyStore.models.Address import Address

class addressRegister(ModelForm):

    class Meta:
        model = Address
        fields = ('street_line1', 'street_line2', 'city', 'county', 'postcode')