from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Accounts.models import User, Profile


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("username", "is_staff", "is_active", "is_verified")
    list_filter = ("username", "is_staff", "is_active", "is_verified")
    searching_fileds = ("username",)
    ordering = ("username",)
    fieldsets = (
        ("Main", {"fields": ("username", "password")}),
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
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["user", "Name", "Family", "Sex"]

    def get_list_display(self, request):
        return ["user", "Name", "Family", "Sex"]

    def get_search_fields(self, request):
        return ["user", ]

    def get_list_filter(self, request, filters=None):
        return ["user", ]
