# Generated by Django 4.0 on 2021-12-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[(1, 'Pago'), (0, 'Devendo')], max_length=1),
        ),
    ]
