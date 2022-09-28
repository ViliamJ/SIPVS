from django import forms


class carForm(forms.Form):
    spz = forms.CharField(label='SPZ', max_length=7)


from formular_web.models import MyContact


class ContactForm(forms.ModelForm):
    class Meta:
        model = MyContact
        fields = ['contact_name', 'contact_group', 'phone', 'email', ]
        widgets = {
            'contact_name': forms.TextInput(attrs={'required': True}),
            'phone': forms.TextInput(attrs={'required': True}),
            'Email': forms.EmailInput(attrs={'required': True}),

        }
