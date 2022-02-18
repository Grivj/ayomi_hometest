from django import forms
from django.contrib.auth.models import User


class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["email"]
