# Generated by Django 4.2.13 on 2024-06-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_remove_services_content_en_remove_services_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
