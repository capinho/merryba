from client.models import Client
from django.contrib.auth.models import User
from .models import Invoice
from django import forms
from datetime import date
from invoice import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(),empty_label="Choisissez le Client")
    types = forms.ChoiceField(choices=Invoice.TYPES)
    formule = forms.ChoiceField(choices=Invoice.FORMULE)
    status = forms.ChoiceField(choices=Invoice.STATUS)
    description = forms.CharField(widget = forms.Textarea)
    # due_date = forms.DateField(
    #     input_formats=settings.DATE_INPUT_FORMATS,
    #     widget=forms.DateInput,
    #     initial=date.today().strftime('%d/%m/%Y')
    # )

    class Meta:
        model = Invoice
        fields = '__all__'



class EditInvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['invoice_number','montant']

class EditUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'is_active', 'is_staff']
