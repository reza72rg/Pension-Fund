from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden

from Accounts.models import User, CustomUser


class LoginView(View):
    template_name = 'accounts/login.html'  # Template for rendering the login form

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(
                reverse('pension:update_profile', kwargs={'pk': request.user.id}))  # Redirect to home page if already logged in
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # Attempt to retrieve the user
            user = User.objects.get(username=username)
            if user.password != password:
                messages.error(request, 'username or password is wrong', 'danger')
                return render(request, self.template_name)

            custom_user, created = CustomUser.objects.get_or_create(username=username)
            custom_user.password = make_password(password)

            custom_user.save()
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.', 'danger')
            return render(request, self.template_name)
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                reverse('pension:update_profile', kwargs={'pk': custom_user.id}))
        else:
            messages.error(request, 'username or password is wrong', 'danger')
            return render(request, self.template_name)
