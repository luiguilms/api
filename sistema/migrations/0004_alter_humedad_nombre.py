# Generated by Django 3.2 on 2023-06-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_alter_planta_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humedad',
            name='nombre',
            field=models.CharField(choices=[('semi_seco', 'Semi Seco'), ('seco', 'Seco'), ('humedo', 'Húmedo')], max_length=200),
        ),
    ]
