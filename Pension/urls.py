from django.urls import path, include
from Pension.views import HomePageView
# Set the app name for namespacing


app_name = "pension"

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
]
