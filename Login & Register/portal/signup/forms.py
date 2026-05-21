from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUPForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        min_length=1,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "User Name",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        max_length=250,
        min_length=1,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        )
    )

    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder": "yyyy-mm-dd",
                "class": "form-control"
            }
        )
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
