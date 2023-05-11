from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from users.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('user/', CustomLoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/home.html'), name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)