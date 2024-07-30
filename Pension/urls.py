from django.urls import path, include
from Pension.views import HomePageView, ProfileEditView
# Set the app name for namespacing


app_name = "pension"

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("profile/<int:pk>/", ProfileEditView.as_view(), name="profile_edit"),
]
