from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),



]
