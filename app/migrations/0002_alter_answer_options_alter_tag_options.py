# Generated by Django 5.0.1 on 2024-01-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Reponse'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Statu'},
        ),
    ]
