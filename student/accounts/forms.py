from django import forms
from models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            "birth_date",
            "short_description",
            "programming_languages")
