from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"
    redirect_authenticated_user = True  # Redirect to success URL if user is already authenticated

    def get_success_url(self):
        return reverse_lazy('pension:home_page')
