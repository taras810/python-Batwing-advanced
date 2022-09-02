from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.is_superuser = False
        instance.is_staff = False
        instance.is_active = True
        if commit:
            instance.save()
        return instance
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
