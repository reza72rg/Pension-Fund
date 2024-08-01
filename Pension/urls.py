from django.urls import path, include
from Pension.views import HomePageView, UpdateProfileView
# Set the app name for namespacing


app_name = "pension"

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    # path("profile/<int:pk>/", ProfileEditView.as_view(), name="profile_edit"),
    path('profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
]
