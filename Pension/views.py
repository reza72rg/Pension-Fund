from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


# Create your views here.


class HomePageView(LoginRequiredMixin, View):
    pass