from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from Accounts.managers import UserManager


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255, unique=True
    )  # username field for user authentication
    is_staff = models.BooleanField(
        default=False
    )  # Boolean field to indicate if user is staff or not
    is_active = models.BooleanField(
        default=True
    )  # Boolean field to indicate if user is active or not
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = []  # Required fields for user registration
    USERNAME_FIELD = "username"  # Field to use for user authentication

    create_date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when user was created
    update_date = models.DateTimeField(
        auto_now=True
    )  # Date and time when user was last updated

    objects = UserManager()  # Manager for user model

    def __str__(self):
        return self.username


# Profile Model
class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Foreign key relation with User model
    Name = models.CharField(max_length=255, blank=True, null=True)
    Family = models.CharField(max_length=255, blank=True, null=True)
    Sex = models.BooleanField(default=False)
    create_date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when profile was created
    update_date = models.DateTimeField(
        auto_now=True
    )  # Date and time when profile was last updated

    def __str__(self):
        return self.user


# Signal to create profile when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
