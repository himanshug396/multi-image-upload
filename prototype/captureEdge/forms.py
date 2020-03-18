from django import forms
from django.db import models
from .models import *

class ImageForm(forms.Form):
	photo = forms.ImageField()