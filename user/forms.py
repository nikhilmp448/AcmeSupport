from random import choices
from unicodedata import name
from django import forms
from django.db import models
from django.db.models import fields


from department.models import Department
from .models import Account


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','email','Phone_Number','Department','password','is_admin']
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
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

class CreateTicket(forms.Form):
    CHOICE = (
        ('high','high'),
        ('medium','medium'),
        ('low','low'),
    )
    subject = forms.CharField(max_length=200)
    description = forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    priority = forms.ChoiceField(choices=CHOICE)
    email = forms.CharField(max_length=100)
    Phone_Number = forms.CharField(max_length=100)
        
    def __init__(self, *args, **kwargs):
        super(CreateTicket, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
