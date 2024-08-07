# Generated by Django 4.2.13 on 2024-06-13 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_bg', models.CharField(max_length=250, null=True)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('content_bg', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
                ('featured', models.BooleanField(default=False)),
                ('date_create', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
