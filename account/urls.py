from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
 # Login / Logout Views
 path('login/', auth_views.LoginView.as_view(), name='account-login'),
 path('logout/', auth_views.LogoutView.as_view(), name='account-logout'),

 # change password views
 path('password-change/', auth_views.PasswordChangeView.as_view(), name='account-password-change'),
 path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='account-password-change-done'),

 # Function Base Views
 path('', views.dashboard, name='account-dashboard'),
]