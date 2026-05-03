from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from allauth.account.views import confirm_email
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Redirect root URL to the login page
def redirect_to_login(request):
    return redirect('/accounts/login/')  # Redirect the root URL to the login page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs for Google login
    path('', redirect_to_login),  # Redirect the root URL to the login page
    path('dashboard/', include('cnTorrent.urls')),  # Include cnTorrent URLs under /dashboard/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)