from django import  forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','password')


    def save(self,commit=True):
        hash = super().save(commit)
        hash.set_password(self.cleaned_data['password'])
        hash.save()






class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'custom_password'}),
    )


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','user_img',)


class EditProfileUsersForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','is_superuser','user_img')