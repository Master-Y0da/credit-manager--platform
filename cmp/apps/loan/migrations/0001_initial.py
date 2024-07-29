# Generated by Django 4.2.14 on 2024-07-28 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('external_id', models.CharField(max_length=255, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('contract_version', models.CharField(max_length=255, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1)),
                ('outstanding', models.IntegerField(default=0)),
                ('maximum_payment_date', models.DateTimeField(null=True)),
                ('taken_at', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='customer.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]