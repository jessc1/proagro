# Generated by Django 3.2.6 on 2021-08-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isencao', '0002_perda_lavoura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perda',
            name='produtor_data_colheita',
            field=models.DateField(null=True, verbose_name='Data da colheita do produtor'),
        ),
    ]
