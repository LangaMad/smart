from django.db import models

from ..choices import SEX_TYPE_CHOICES
from ..invoices.models import BaseModel
# Create your models here.


class Client(BaseModel):
    inn = models.CharField(max_length=20, null=True,blank=True,verbose_name="ИНН")
    email = models.EmailField(null=True,blank=True,verbose_name="Email")
    legal_address = models.CharField(max_length=255,null=True,blank=True,verbose_name="Юридический адрес")
    street = models.CharField(max_length=255,null=True,blank=True,verbose_name="Улица")
    home = models.CharField(max_length=50,null=True,blank=True,verbose_name="Дом")
    scan_notarius = models.FileField(upload_to='documents/scan/',verbose_name='Cкан нотариально заверенного перевода паспорта',
    blank=True, null=True, max_length=500)
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.inn or f"Клиент {self.pk}"


class Passport(models.Model):
    passport_series = models.CharField(max_length=250,null=True,blank=True,verbose_name="Серия паспорта")
    document_number = models.CharField(max_length=250,null=True,blank=True,verbose_name="Номер документа")
    inn = models.CharField(max_length=220,null=True,blank=True,verbose_name="ИНН")
    issuing_authority = models.CharField(max_length=255,verbose_name="Орган выдачи",blank=True,null=True)
    issued_date = models.DateField(verbose_name='Дата выдачи', blank=True, null=True )
    expiration_date = models.DateField( verbose_name='Дата окончания действия',blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    sex = models.CharField(max_length=25,choices=SEX_TYPE_CHOICES,  verbose_name='Пол', blank=True, null=True)
    country = models.CharField(max_length=255,verbose_name="Страна",blank=True,null=True)
    country_citizenship = models.CharField(  max_length=255,verbose_name="Страна гражданства",blank=True,null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name="Клиент", null=True, blank=True)
    front_photo = models.FileField( upload_to='documents/front/',verbose_name='Передняя сторона документа',
                                    blank=True, null=True, max_length=500)
    back_photo = models.FileField(upload_to='documents/back/',verbose_name='Задняя сторона документа',
                                  blank=True, null=True,max_length=500)

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"

    def __str__(self):
        return f"{self.passport_series or ''} {self.document_number or ''}".strip()




