from django.contrib.auth import admin

__all__ = ["UserAdmin"]


class UserAdmin(admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("countryCode", "mobileNumber", "password", "email")}),
        ("Personal info", {"fields": ("firstName", "lastName", "dateOfBirth", "nic")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "firstName", "lastName", "password1", "password2"),
            },
        ),
    )
    list_display = ("__str__", "mobileNumber", "firstName", "lastName", "is_staff")
    search_fields = ("mobileNumber", "firstName", "lastName")
    ordering = ("date_joined",)
    readonly_fields = ("last_login", "date_joined")
    list_display_links = ("__str__",)
