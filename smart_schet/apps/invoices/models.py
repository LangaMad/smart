from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, related_name="created_%(class)s", on_delete=models.SET_NULL,
                                   null=True,verbose_name='Создано пользователем')
    updated_by = models.ForeignKey(User, related_name="updated_%(class)s", on_delete=models.SET_NULL,
                                   null=True,verbose_name='Обновлено пользователем')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата обновления')

    class Meta:
        abstract = True
        verbose_name = 'Базовая информация'
        verbose_name_plural = 'Базовая информация'




class Invoice(BaseModel):
    company_name = models.CharField(max_length=255,null=True,blank=True,verbose_name="Название компании")
    invoice_number = models.CharField(max_length=255,null=True,blank=True,verbose_name="Номер счёта")
    inn = models.CharField(max_length=220,null=True,blank=True,verbose_name="ИНН")
    client_type = models.CharField(max_length=250,default='legal',verbose_name="Тип клиента")
    amount = models.DecimalField( max_digits=20,decimal_places=2,verbose_name="Сумма")
    amount_paid = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="Оплачено" )
    date_of_paid = models.DateField(verbose_name="Дата оплаты")

    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"

    def __str__(self):
        return f"Счёт {self.invoice_number}"


class Product(models.Model):
    product_number = models.CharField(max_length=250,null=True,blank=True,verbose_name="Номер продукта")
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Цена",null=True,blank=True)
    quantity = models.IntegerField(verbose_name="Количество", null=True, blank=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Общая сумма", null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


    def __str__(self):
        return f"Продукт {self.pk}"







