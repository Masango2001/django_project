from django import forms
from django.models import student
class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','surname','email','age']