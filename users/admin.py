from django.contrib import admin
from users.models import Contact, Profile, UrlData

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(UrlData)