# Generated by Django 4.0.5 on 2022-06-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_ad_photo_alter_ad_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
