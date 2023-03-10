# Generated by Django 4.1.5 on 2023-01-24 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_type_name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_type_name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HeadlinerTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patio_code', models.PositiveIntegerField()),
                ('patio_code_group', models.PositiveIntegerField()),
                ('promo_name', models.CharField(max_length=255)),
                ('date_begin', models.DateField(auto_now_add=True)),
                ('date_over', models.DateField()),
                ('price_old', models.IntegerField(null=True)),
                ('price_new', models.IntegerField(null=True)),
                ('budget', models.IntegerField()),
                ('sales_plan', models.IntegerField()),
                ('utm', models.CharField(max_length=255)),
                ('budget_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='headliner.budget')),
                ('promo_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='headliner.promo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
        ),
    ]
