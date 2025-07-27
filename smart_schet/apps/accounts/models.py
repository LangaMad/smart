from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Abilities(models.Model):
    abilities_name = models.CharField(max_length=255,null=True, blank=True,verbose_name="Название")

    class Meta:
        verbose_name = "Способность"
        verbose_name_plural = "Способности"

    def __str__(self):
        return self.abilities_name

class Role(models.Model):
    role_name = models.CharField(max_length=255,null=True, blank=True,verbose_name="Название Роли")
    abilities = models.ManyToManyField(Abilities, related_name="roles")

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.role_name


class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,verbose_name="Роль", null=True, blank=True,)
    phone_number= models.CharField(max_length=230,verbose_name='Номер телефона клиента',blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username} ({self.role})"