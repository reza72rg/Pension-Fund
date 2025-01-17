from django.urls import path, include, reverse_lazy
from Accounts.views import LoginView
from django.contrib.auth.views import LogoutView
# Set the app name for namespacing

app_name = "accounts"


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),

    # Logout view
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('pension:home_page')), name='logout'),
]
