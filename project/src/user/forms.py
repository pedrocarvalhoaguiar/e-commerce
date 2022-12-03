from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if CustomUser.objects.filter(email=email).first():
            raise forms.ValidationError(f"Email {email} já está em uso")
        return email


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserLoginForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
