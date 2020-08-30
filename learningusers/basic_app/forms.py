from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileInfo


def check_email_providers(email_address):
    banned_hosts = ['hotmail', 'company.com']
    for address in banned_hosts:
        if address in email_address:
            raise forms.ValidationError(f'Currently we cannot accept {address} emails. please try another email')



# class UserForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput
#     )
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        validators=[check_email_providers],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]



class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = [
            'portfolio_site',
            'profile_pic',
        ]