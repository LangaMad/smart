from django.db import models
from ..invoices.models import BaseModel
# Create your models here.


class Client(BaseModel):
    inn = models.CharField(max_length=20, null=True,blank=True,verbose_name="ИНН")
    email = models.EmailField(null=True,blank=True,verbose_name="Email")
    legal_address = models.CharField(max_length=255,null=True,blank=True,verbose_name="Юридический адрес")
    street = models.CharField(max_length=255,null=True,blank=True,verbose_name="Улица")
    home = models.CharField(max_length=50,null=True,blank=True,verbose_name="Дом")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.inn or f"Клиент {self.pk}"


class Passport(models.Model):
    passport_series = models.CharField(max_length=250,null=True,blank=True,verbose_name="Серия паспорта")
    document_number = models.CharField(max_length=250,null=True,blank=True,verbose_name="Номер документа")
    inn = models.CharField(max_length=220,null=True,blank=True,verbose_name="ИНН")

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"

    def __str__(self):
        return f"{self.passport_series or ''} {self.document_number or ''}".strip()




