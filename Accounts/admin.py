from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Accounts.models import CustomUser, User


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("username", "name", "family", "sex", "is_staff", "is_active", "is_verified")
    list_filter = ("username", "is_staff", "is_active", "is_verified")
    searching_fileds = ("username",)
    ordering = ("username",)
    fieldsets = (
        ("Main", {"fields": ("username", "password", "name", "family", "sex")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("important date", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "name",
                    "family",
                    "sex",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["username", "name", "family", "sex"]

    def get_list_display(self, request):
        return ["username", "name", "family", "sex"]

    def get_search_fields(self, request):
        return ["username", ]

    def get_list_filter(self, request, filters=None):
        return ["username", ]