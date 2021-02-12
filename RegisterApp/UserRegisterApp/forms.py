from django import forms
from .models import RegisteredUser


class RegisterationForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = [
            'email_address',
            'first_name',
            'middle_name',
            'last_name',
            'country_of_residence',
            'contact_number',
            'willingness_to_join_session',
            'comments'
        ]