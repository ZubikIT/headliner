# Generated by Django 4.1.5 on 2023-01-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headliner', '0002_alter_headlinertable_budget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlinertable',
            name='choice_input',
            field=models.BooleanField(default=True),
        ),
    ]
