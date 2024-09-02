# Generated by Django 5.1 on 2024-09-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_productout'),
    ]

    operations = [
        migrations.AddField(
            model_name='productout',
            name='amountOut',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productout',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productout',
            name='quantityOut',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
