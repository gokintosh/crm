from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *

from .forms import OrderForm

# Create your views here.

def home(request): 
    customers=Customer.objects.all()
    orders=Order.objects.all()

    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'customers':customers,'orders':orders,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def about(request):
    products=Products.objects.all()
    return render(request,'accounts/about.html',{'products':products})

def customers(request,pk):
    customer=Customer.objects.get(id=pk)

    orders=customer.order_set.all()
    total_orders=orders.count()

    context={'customer':customer,'orders':orders,'total_order':total_orders}
    return render(request,'accounts/customers.html',context)

def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'))
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(instance=customer)
    form=OrderForm(initial={'customres':customer})
    if request.method=='POST':
        # print('Printing Post:',request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'formset':formset}
    return render(request,'accounts/order_form.html',context)


def updateOrder(request,pk_test):

    order=Order.objects.get(id=pk_test)

    form=OrderForm(instance=order)
    if request.method=='POST':
    # print('Printing Post:',request.POST)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'accounts/delete.html',context)