# Generated by Django 4.2.2 on 2023-06-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_producto_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
