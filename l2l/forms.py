from django import forms
from .models import *

class image_upload(forms.ModelForm):
    class Meta:
        model = image_upload
        fields = ['name','img']