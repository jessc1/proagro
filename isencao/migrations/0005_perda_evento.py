# Generated by Django 3.2.6 on 2021-08-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isencao', '0004_alter_perda_produtor_data_colheita'),
    ]

    operations = [
        migrations.AddField(
            model_name='perda',
            name='evento',
            field=models.CharField(choices=[('I', 'CHUVA EXCESSIVA'), ('II', 'GEADA'), ('III', 'GRANIZO'), ('IV', 'SECA'), ('V', 'VENDAVAL'), ('VI', 'RAIO')], max_length=30, null=True),
        ),
    ]