from unicodedata import name
from django import forms
from django.db import models
from django.db.models import fields

from department.models import Department
from .models import Account


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','email','Phone_Number','Department','is_admin']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

class CreateDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Name','Description']
    
    def __init__(self, *args, **kwargs):
        super(CreateDepartment, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
