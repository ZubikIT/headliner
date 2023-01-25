# Generated by Django 4.1.5 on 2023-01-24 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('headliner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlinertable',
            name='budget',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='headlinertable',
            name='patio_code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='headlinertable',
            name='price_new',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='headlinertable',
            name='price_old',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='headlinertable',
            name='sales_plan',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='headlinertable',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
