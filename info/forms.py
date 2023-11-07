import re
from django import forms
from .models import *


class ClassDetailsForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name',]
        