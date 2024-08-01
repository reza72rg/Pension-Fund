from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from Accounts.models import User, Profile

# Create your views here.


class HomePageView(LoginRequiredMixin, View):
    pass


class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'pension/index.html'
    model = Profile
    fields = ['name', 'family', 'sex']
    success_url = reverse_lazy('pension:home_page')

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # Get the pk from kwargs
        if request.user.id != int(pk):  # Ensure pk is cast to int
            return redirect('pension:home_page')  # Correct return statement
        return super().dispatch(request, *args, **kwargs)  # Call the superclass dispatch

    def form_valid(self, form):
        value = self.request.POST['user']
        username = get_object_or_404(User, username=self.request.user)
        username.username = value
        username.save()
        return super(UpdateProfileView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = User.objects.get(username=self.request.user)
        return context
