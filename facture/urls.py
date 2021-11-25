"""invoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),

    
    path('users/', views.liste_utilisateur, name='users'),
    path('deleteuser/<str:pk>', views.deleteUser, name='delete_user'),
    path('editUser/<str:pk>', views.updateUser, name='update_user'),


    path('createInvoice/', views.createInvoice, name='createInvoice'),
    path('allinvoices/', views.InvoiceList, name='allinvoices'),
    path('deleteInvoice/<str:pk>', views.deleteInvoice, name='delete_invoice'),
    path('updateInvoice/<str:pk>', views.updateInvoice, name='update_invoice'),


    path('pdf_view/<str:pk>/', views.ViewPDFd, name="pdf_view"),
    path('pdf_download/<str:pk>/', views.DownloadPDF, name="pdf_download"),


]
