from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    company = models.ForeignKey('Company', on_delete=CASCADE)
    subdivision = models.ForeignKey('Subdivision', on_delete=CASCADE)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Company(models.Model):
    parent = models.ForeignKey('Company', on_delete=CASCADE)


class Subdivision(models.Model):
    parent = models.ForeignKey('Subdivision', on_delete=CASCADE)
    company = models.ForeignKey('Company', on_delete=CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=50)


class LicArea(models.Model):
    title = models.CharField(max_length=50)
    project = models.ManyToManyField(Project)


class Deposit(models.Model):
    title = models.CharField(max_length=50)
    lic_area = models.ManyToManyField(LicArea)


class Object(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('Object', on_delete=CASCADE)

