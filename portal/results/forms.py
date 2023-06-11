from django import forms
from django.contrib.auth.models import User

from . import models

class StudentLoginForm(forms.Form):
    reg_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

