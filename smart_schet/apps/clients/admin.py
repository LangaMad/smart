from django.contrib import admin
from .models import Client, Passport

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("inn", "email", "legal_address", "street", "home", "created_by", "created_at")
    search_fields = ("inn", "email", "legal_address", "street")
    list_filter = ("created_at",)


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ("passport_series", "document_number", "inn")
    search_fields = ("passport_series", "document_number", "inn")
