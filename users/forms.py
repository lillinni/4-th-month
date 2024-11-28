from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomRegistrationForm(UserCreationForm):
    LEVELS = (
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    )
    level = forms.ChoiceField(choices=LEVELS, required=True, label="Qualification Level")

    class Meta:
        model = models.CustomUser
        fields = ["username", "first_name", "last_name", "level", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.level = self.cleaned_data["level"]
        if commit:
            user.save()
        return user
