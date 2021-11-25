# Generated by Django 3.1.5 on 2021-11-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='types',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE')], default='CASH', max_length=100),
        ),
    ]
