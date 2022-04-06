from django import forms

from .models import DVD

class DVDCreate(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ["title","category","runTime","year","price",]