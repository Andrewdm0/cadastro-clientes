# Generated by Django 4.0 on 2021-12-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_cliente_data_alter_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
