from io import BytesIO, StringIO
from django.contrib.auth.models import User
from django.http import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from client.models import Client
from facture.models import Invoice
from .forms import EditInvoiceForm, EditUserForm, InvoiceForm
import datetime
from django.views.generic import UpdateView
from django.views import View
from django.template.loader import get_template
from xhtml2pdf import pisa
from invoice import settings
import os

# Create your views here.

def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception('media URI must start with %s or %s' % (sUrl, mUrl))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result,link_callback=link_callback)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



def ViewPDFd(request, pk):

    data = get_object_or_404(Invoice, id=pk)
    context = {
        'data':data
    }
    pdf = render_to_pdf('facture/pdf_template2.html', context)

    return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file

def DownloadPDF(request, pk):
    data = get_object_or_404(Invoice, id=pk)
    context = {
        'data':data
    }

    pdf = render_to_pdf('facture/pdf_template2.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Invoice_%s.pdf" %(data.invoice_number)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Vous êtes maintenant connecté.')

            return redirect('home')

        else:
            messages.error(request, 'Identifiants de connexion non valides')
            return redirect('login')
    return render(request, 'facture/login.html')

@login_required
def home(request):
    user = request.user
    context = {'user':user}
    return render(request, 'index.html', context)

######################################--USER--#############################################################
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Vous êtes maintenant déconnecté.')
    return redirect('login')

@login_required
def liste_utilisateur(request):
    users = User.objects.all()
    return render(request,'app-users.html',{'users':users})

@login_required
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'user':user}
    return render(request, 'user/deleteuser.html', context)

@login_required
def updateUser(request, pk):
    user = User.objects.get(id=pk)    
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()   
            return redirect('users')
    context = {'form':form}
    return render(request, 'user/updateuser.html', context)

####################################################################################################
@login_required
def InvoiceList(request):
    invoices = Invoice.objects.all()
    context = {
        "invoices":invoices,
    }
    return render(request, 'facture/acc-invoices.html', context)
@login_required
def createInvoice(request):
    invoices = Invoice.objects.all()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = Invoice()

            data.types = form.cleaned_data['types']
            data.client = form.cleaned_data['client']
            data.description = form.cleaned_data['description']
            data.formule = form.cleaned_data['formule']
            data.status = form.cleaned_data['status']
          #  data.due_date = form.cleaned_data['due_date']
             #montant a payer
            if data.formule == 'Seance unique':
                data.montant = 35000
            else:
                data.montant = 150000
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%d%m%Y") #20210305
            invoice_number = 'IMB-'+current_date + str(data.id)
            data.invoice_number = invoice_number

           
            data.save()

            return redirect('allinvoices')
    else:
        form = InvoiceForm()

    context = {
        'invoices':invoices,
        'form': form
    }

    return render(request, 'facture/createInvoice.html', context)

@login_required
def deleteInvoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('allinvoices')
    context = {'i':invoice}
    return render(request, 'facture/deleteInvoice.html', context)

@login_required
def updateInvoice(request, pk):
    invoice = Invoice.objects.get(id=pk)    
    form = EditInvoiceForm(instance=invoice)
    if request.method == 'POST':
        form = EditInvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            my_obj = form.save()

            if my_obj.formule == 'Seance unique':
                my_obj.montant = 35000
            else:
                my_obj.montant = 150000
            my_obj.save()
                
            return redirect('allinvoices')
    context = {'form':form}
    return render(request, 'facture/updateInvoice.html', context)



def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response
