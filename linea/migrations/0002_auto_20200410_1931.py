# Generated by Django 2.1.5 on 2020-04-10 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hito',
            name='question',
        ),
        migrations.DeleteModel(
            name='Etiqueta',
        ),
        migrations.DeleteModel(
            name='Hito',
        ),
    ]
