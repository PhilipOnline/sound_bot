from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user