# Generated by Django 4.0 on 2021-12-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('Pago', 'Pago'), ('Devendo', 'Devendo')], max_length=7),
        ),
    ]
