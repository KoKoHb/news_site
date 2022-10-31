from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, Category


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "article", "image", "category")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "article": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class UserRegister(UserCreationForm):
    username = forms.CharField(max_length=150,
                               label="Имя пользователя",
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "autocomplete": "off",
                                                             "placeholder": "допускаются буквы, цифры и символы . - _ +"}))
    email = forms.EmailField(required=True,
                             label="Email",
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "autocomplete": "off", }))
    password1 = forms.CharField(min_length=8,
                                label="Пароль",
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "autocomplete": "off",
                                                                  "placeholder": "Пожалуйста, придумайте сложный пароль. Минимум 8 символов"}))
    password2 = forms.CharField(min_length=8,
                                label="Повтор пароля",
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "autocomplete": "off",
                                                                  "placeholder": "Введите пароль еще раз"}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ("username", "email")


class UserLogin(AuthenticationForm):
    username = forms.CharField(max_length=150,
                               label="Имя пользователя",
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "autocomplete": "off",
                                                             "placeholder": "Введите ваше имя пользователя"}))
    password = forms.CharField(min_length=8,
                               label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "autocomplete": "off",
                                                                 "placeholder": "Введите ваш пароль"}))

