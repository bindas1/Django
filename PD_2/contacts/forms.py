from django import forms

from contacts.models import Person, EmailField


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender']


class EmailFieldForm(forms.ModelForm):
    class Meta:
        model = EmailField
        fields = ['owner', 'email', 'role']
