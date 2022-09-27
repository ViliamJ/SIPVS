from django import forms

class carForm(forms.Form):
    spz = forms.CharField(label='SPZ', max_length=7)