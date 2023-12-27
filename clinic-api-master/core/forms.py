from django import forms
from django.core.exceptions import ValidationError

class ResetPassword(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "class": "focus:shadow-soft-primary-outline text-size-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow"
            }
        )
    )
    re_new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "focus:shadow-soft-primary-outline text-size-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()  
        new_password1 = cleaned_data.get('new_password')
        new_password2 = cleaned_data.get('re_new_password')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
