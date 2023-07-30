from django.contrib import admin
from django.urls import path
from home import views

from django.contrib.auth import views as auth_views
from home.forms import LoginForm

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('login/', views.loginUser, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # path('register/', views.RegisterUser, name='register'),
    path('register/', views.CustomerRegistrationView.as_view(), name="register"),
    path('save_contact', views.save_contact, name='save_contact'),
    path('home_save', views.home_save, name='home_save'),
    path('logout/', views.logoutUser, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
