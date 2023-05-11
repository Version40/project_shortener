from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ContactForm, Url
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from .models import UrlData


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)

def home(request):
    return render(request, 'users/home.html')

def info(request):
    return render(request, 'users/info.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            theme = form.cleaned_data['theme']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'Тема: {}'.format(theme),
                message,
                'ivan.mikityuk4@gmail.com',  # Send from (your website)
                ['ivan.mikityuk4@gmail.com'],  # Send to (your admin email)
                [],
                reply_to=[email]  # Email from the form to get back to
            ).send()

        return redirect('home')

    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form': form})

@login_required
def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            slug = form.cleaned_data["slug"]
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug, name=name, user=request.user)
            new_url.save()
            return redirect('short')
    else:
        form = Url()
    data = UrlData.objects.filter(user=request.user).all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'users/short.html', context)


def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)