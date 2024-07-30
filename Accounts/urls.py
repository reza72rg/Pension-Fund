from django.urls import path, include
from Accounts.views import CustomLoginView
from django.contrib.auth.views import LogoutView
# Set the app name for namespacing


app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    # Logout view
    path('logout/', LogoutView.as_view(), name='logout'),
]
