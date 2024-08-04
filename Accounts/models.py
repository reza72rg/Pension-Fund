from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from Accounts.managers import UserManager


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255, unique=True
    )  # username field for user authentication
    name = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    sex = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False
    )  # Boolean field to indicate if user is staff or not
    is_active = models.BooleanField(
        default=True
    )  # Boolean field to indicate if user is active or not
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)  # Include last_login field
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

    class Meta:
        db_table = 'Custom_User'  # Specify the custom table name here


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)  # username field for user authentication
    USERNAME_FIELD = 'username'  # Define the USERNAME_FIELD
    name = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    sex = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)  # Include last_login field
    is_staff = models.BooleanField(
        default=False
    )  # Boolean field to indicate if user is staff or
    is_active = models.BooleanField(
        default=True
    )  # Boolean field to indicate if user is active or not
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='Custom_User_set',  # Modify this name as desired
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='Custom_User_permissions_set',  # Modify this name as desired
        blank=True
    )

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'user'  # Specify the custom table name here

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.last_login:
            self.last_login = timezone.now()  # Update last_login when the user logs in
        super().save(*args, **kwargs)
