from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from Accounts.models import CustomUser

# Create your views here.


class HomePageView(LoginRequiredMixin, View):
    pass


class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'pension/index.html'
    model = CustomUser
    fields = ['username', 'name', 'family', 'sex']
    success_url = reverse_lazy('pension:home_page')
    context_object_name = 'user'  # Custom context object name

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # Get the pk from kwargs
        if request.user.id != int(pk):  # Ensure pk is cast to int
            return redirect('pension:home_page')  # Correct return statement
        return super().dispatch(request, *args, **kwargs)  # Call the superclass dispatch

    def form_valid(self, form):
        # Perform additional actions here if needed before saving
        return super().form_valid(form)

    def form_invalid(self, form):
        # This is where the form is invalid
        context = self.get_context_data(form=form)  # Get the context with form data
        # You can also add any additional context here if needed
        return self.render_to_response(context)  # Render the response with the invalid form
