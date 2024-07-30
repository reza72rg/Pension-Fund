from django import forms
from Accounts.models import User, Profile
from django.core.exceptions import ValidationError


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'family', 'sex']
