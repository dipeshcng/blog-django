from django import forms
from .models import *
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'gallery', 'description', 'organizer', 'venue']


class ContactForm(forms.Form):
    sender = forms.CharField(widget=forms.TextInput())
    mobile_number = forms.CharField(widget=forms.NumberInput())
    email = forms.CharField(widget=forms.EmailInput())
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password didn't match")

        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        users = User.objects.filter(username=username)

        if users.exists():
            raise forms.ValidationError("user already exists")

        return username
