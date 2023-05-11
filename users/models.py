import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

class Contact(models.Model):
    theme = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UrlData(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Link")
    url = models.CharField(max_length=200)
    slug = models.CharField(
        unique=True,
        default=uuid.uuid1,
        max_length=15,
        error_messages={
            "unique":"The Field you entered is not unique."
        }
    )

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"

