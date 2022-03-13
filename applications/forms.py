from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from applications.models import Application


class ApplicationForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {   
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows':'2'}),
        }  

    def clean_dob(self):
        birthdate = self.cleaned_data['dob']
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age < 18:
            raise ValidationError("You must be 18 years old or older to fill this form")

        return birthdate