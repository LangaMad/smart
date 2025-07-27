from django.contrib import admin
from .models import User, Role, Abilities
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("full_name", "role", "phone_number")}),
    )
    list_display = ("username", "full_name", "role", "phone_number", "is_staff", "is_active")
    search_fields = ("username", "full_name", "phone_number")
    list_filter = ("role", "is_staff", "is_active")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name")
    search_fields = ("role_name",)
    filter_horizontal = ("abilities",)


@admin.register(Abilities)
class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ("id", "abilities_name")
    search_fields = ("abilities_name",)
