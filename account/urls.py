from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
 path('login/', auth_views.LoginView.as_view(), name='account-login'),
 path('logout/', auth_views.LogoutView.as_view(), name='account-logout'),
 path('', views.dashboard, name='account-dashboard'),
]