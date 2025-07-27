from django.contrib import admin
from .models import Invoice, Product
# Register your models here.

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "company_name", "inn", "client_type", "amount",
                    "amount_paid", "date_of_paid", "created_by", "created_at")
    list_filter = ("client_type", "date_of_paid")
    search_fields = ("invoice_number", "company_name", "inn")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_number")
    search_fields = ("product_number",)