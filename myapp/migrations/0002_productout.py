# Generated by Django 5.1 on 2024-09-01 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityOut', models.PositiveIntegerField()),
                ('dateOut', models.DateTimeField(auto_now_add=True)),
                ('product_out', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.products')),
            ],
        ),
    ]
