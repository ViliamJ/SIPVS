import labels as labels
from django import forms
from formular_web.models import MyCar


class CarForm(forms.ModelForm):
    class Meta:
        model = MyCar
        fields = ['first_name', 'second_name', 'ID_number', 'email', 'car_brand', 'car_type', 'spz', 'registration_date', 'vin']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'second_name': forms.TextInput(attrs={'required': True}),
            'ID_number': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'car_brand': forms.TextInput(attrs={'required': True}),
            'spz': forms.TextInput(attrs={'required': True}),
            'registration_date': forms.SelectDateWidget(attrs={'required': True}),
            'vin': forms.NumberInput(attrs={'required': True}),
        }