# Generated by Django 2.1.5 on 2020-04-11 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_auto_20200411_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentosoficiales',
            options={'verbose_name_plural': 'documentos oficiales'},
        ),
        migrations.AlterModelOptions(
            name='emisor',
            options={'verbose_name_plural': 'emisores'},
        ),
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'verbose_name_plural': 'etiquetas'},
        ),
        migrations.AddField(
            model_name='documentosoficiales',
            name='archivo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]