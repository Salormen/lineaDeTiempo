# Generated by Django 2.1.5 on 2020-04-11 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_auto_20200411_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hito',
            new_name='DocumentosOficiales',
        ),
    ]