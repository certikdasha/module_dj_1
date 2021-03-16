from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView

from app.forms import CustomUserCreationForm
from app.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'index.html'
    login_url = 'login/'


class Login(LoginView):
    success_url = '/'
    template_name = 'login.html'


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
