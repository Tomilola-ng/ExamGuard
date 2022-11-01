from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator


class CustomUserCreationForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","phone")
