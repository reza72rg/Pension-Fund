from django import forms
from Accounts.models import CustomUser
from django.core.exceptions import ValidationError


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'family', 'sex']


