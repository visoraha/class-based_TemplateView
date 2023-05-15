from django import forms
from app.models import *


class student_form(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'