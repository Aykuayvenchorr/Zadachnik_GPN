from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, SET_NULL
from django.db.models.signals import post_save, post_delete
from phonenumber_field.modelfields import PhoneNumberField

from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
from zadachnik.models import Company, Subdivision


class User(ChangeloggableMixin, AbstractUser):
    company = models.ForeignKey(Company, on_delete=SET_NULL, blank=True, null=True, verbose_name='Компания')
    subdivision = models.ForeignKey(Subdivision, on_delete=SET_NULL, blank=True, null=True, verbose_name='Подразделение')
    name = models.CharField(max_length=77, verbose_name='Имя')
    surname = models.CharField(max_length=77, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=77, verbose_name='Отчество')
    position = models.CharField(max_length=77, verbose_name='Должность')
    phone_work = PhoneNumberField(blank=True, verbose_name='Рабочий телефон')
    phone_mob = PhoneNumberField(blank=True, verbose_name='Мобильный телефон')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    note = models.TextField(blank=True, verbose_name='Примечания')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


post_save.connect(journal_save_handler, sender=User)
post_delete.connect(journal_delete_handler, sender=User)