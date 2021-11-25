from django.shortcuts import get_object_or_404, redirect, render
from .models import Client
from .forms import ClientForm, EditClientForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def liste_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'client/client-all.html', context)

@login_required
def addClient(request):
    #url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = Client()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone_number = form.cleaned_data['phone_number']
            data.email = form.cleaned_data['email']
            data.adress = form.cleaned_data['adress']
            data.save()
            return redirect('allClient')
    else:
        form = ClientForm()
    return render(request, 'client/client-add.html', {'form': form})

@login_required
def updateClient(request, pk):
    invoice = Client.objects.get(id=pk)    
    form = EditClientForm(instance=invoice)
    if request.method == 'POST':
        form = EditClientForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()   
            return redirect('allClient')
    context = {'form':form}
    return render(request, 'client/updateclient.html', context)


@login_required
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)    
    if request.method == 'POST':
        client.delete()
        return redirect('allClient')
    context = {'client':client}
    return render(request, 'client/delete.html', context)



