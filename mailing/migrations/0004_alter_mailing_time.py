# Generated by Django 4.2.3 on 2023-07-21 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailing_date_alter_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время начала рассылки (чч:мм:сс)'),
        ),
    ]