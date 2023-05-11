from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

from users.models import Contact, UrlData


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='',
        required=True,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    password1 = forms.CharField(
        label='',
        required=True,
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='',
        # required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='',
        required=True,
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )



    class Meta:
        model = User
        fields = ['username', 'email']


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    theme = forms.CharField(
        label='',
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема письма'})
    )
    email = forms.EmailField(
        label='',
        required=True,
        max_length=150,
    )
    message = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'}),
        max_length=2000,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Email'})

    class Meta:
        model = Contact
        fields = ['theme', 'email', 'message']

class Url(forms.Form):
    name = forms.CharField(
        label='',
        required=False,
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Название'})
    )
    url = forms.CharField(
        label='',
        required=True,
        max_length=300,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ссылку'})
    )
    slug = forms.CharField(
        label='',
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Введите сокращение'})
    )

    def clean_slug(self):
        data = self.cleaned_data.get('slug')
        if UrlData.objects.filter(slug=data).exists():
            raise forms.ValidationError('Такая уникальная запись уже существует!')
        return data

    class Meta:
        model = UrlData
        fields = ['name', 'url', 'slug']
