# Generated by Django 4.2.11 on 2024-05-27 11:02

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('zadachnik', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='lic_area',
        ),
        migrations.RemoveField(
            model_name='licarea',
            name='project',
        ),
        migrations.RemoveField(
            model_name='object',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='subdivision',
            name='company',
        ),
        migrations.RemoveField(
            model_name='subdivision',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=0, max_length=77, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='note',
            field=models.TextField(blank=True, verbose_name='Примечания'),
        ),
        migrations.AddField(
            model_name='user',
            name='patronymic',
            field=models.CharField(default=0, max_length=77, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_mob',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Мобильный телефон'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_work',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Рабочий телефон'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(default=0, max_length=77, verbose_name='Должность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default=0, max_length=77, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zadachnik.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zadachnik.subdivision', verbose_name='Подразделение'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='LicArea',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Subdivision',
        ),
    ]