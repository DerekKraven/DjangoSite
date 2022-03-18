from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['last_name', 'first_name', 'patronymic', 'date_of_birth','series','number','group_name']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={"type": "date"}),
        }

    def clean_series(self):
        series = self.cleaned_data['series']
        if not re.match(r'^[0-9]{4}$', series):
            raise ValidationError('Серия паспорта должна состоять из 4 цифр')
        return series



    def clean_number(self):
        number = self.cleaned_data['number']
        if not re.match(r'^[0-9]{6}$', number):
            raise ValidationError('Номер паспорта должен состоять из 6 цифр')
        return number





class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'number_of_students']


