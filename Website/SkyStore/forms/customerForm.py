__author__ = 'iri03'

from django.forms import ModelForm

from django.contrib.auth.models import User


class Register(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'username')