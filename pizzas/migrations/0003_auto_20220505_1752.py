# Generated by Django 3.2.13 on 2022-05-05 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20220505_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topping',
            new_name='text',
        ),
    ]
