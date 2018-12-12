from django import forms
import PIL
class form(forms.Form):
    image = forms.FileField()
