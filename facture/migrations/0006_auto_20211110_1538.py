# Generated by Django 3.1.5 on 2021-11-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0005_auto_20211108_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='formule',
            field=models.CharField(choices=[('', 'CHOISISSEZ LA FORMULE...'), ('Seance unique', 'Seance unique'), ('Formule 5 seances', 'Formule 5 seances')], default='Seance unique', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('', 'CHOISISSEZ LE STATUS...'), ('NOTPAID', 'NON PAYER'), ('AVOIR', 'AVOIR'), ('PAID', 'PAYER')], default='NOTPAID', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='types',
            field=models.CharField(choices=[('', 'CHOISISSEZ LE TYPES...'), ('CASH', 'CASH'), ('CHEQUE', 'CHEQUE')], default='CASH', max_length=100),
        ),
    ]