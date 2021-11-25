from django.db import models
from client.models import Client
# Create your models here.

class Invoice(models.Model):
    STATUS = [
        ('', 'CHOISISSEZ LE STATUS...'),
        ('NOTPAID', 'NON PAYER'),
        ('AVOIR', 'AVOIR'),
        ('PAID', 'PAYER'),
    ]
    
    FORMULE = [
        ('', 'CHOISISSEZ LA FORMULE...'),
        ('Seance unique', 'Seance unique'),
        ('Formule 5 seances', 'Formule 5 seances'),
    ]

    TYPES = [
        ('', 'CHOISISSEZ LE TYPES...'),
        ('CASH', 'CASH'),
        ('CHEQUE', 'CHEQUE'),
    ] 

    invoice_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,blank=True, null=True)
    #due_date = models.DateField(null=True, blank=True)
    types = models.CharField(choices=TYPES, default='CASH', max_length=100)
    description = models.TextField(default= "this is a default message.")
    formule = models.CharField(choices=FORMULE, default='Seance unique', max_length=100)
    status = models.CharField(choices=STATUS, default='NOTPAID', max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return str(self.client)
    
    def get_status(self):
        return self.status
