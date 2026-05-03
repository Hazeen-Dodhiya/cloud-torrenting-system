from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_torrent/', views.add_torrent, name='add_torrent'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
]
