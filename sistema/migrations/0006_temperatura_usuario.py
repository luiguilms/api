# Generated by Django 3.2 on 2023-06-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_alter_humedad_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
