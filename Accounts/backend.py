from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from Accounts.models import User


class PlaintextPasswordBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            # Check plaintext password
            if user.password == password:
                return user
        except User.DoesNotExist:
            return None
        return None