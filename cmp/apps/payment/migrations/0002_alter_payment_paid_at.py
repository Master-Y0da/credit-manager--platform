# Generated by Django 4.2.14 on 2024-07-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]