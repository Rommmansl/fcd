from django import forms
from vid4.models import Picture


class Pictureform(forms.ModelForm):
    picfile = forms.ImageField()

    class Meta:
        model = Picture
        fields = ('picfile',)


