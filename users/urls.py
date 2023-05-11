from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.register, name='reg'),
    path('accounts/profile/', views.profile, name='profile'),
    path('about/', views.info, name='info'),
    path("contact/", views.contact, name="contact"),
    path("short/", views.urlShort, name="short"),
    path("short/<str:slugs>", views.urlRedirect, name="redirect")
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )