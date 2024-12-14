from django.http import HttpResponse
from django.shortcuts import render
from .models import Ride
from django.shortcuts import redirect, render

# Create your views here.
def tableaux_C(request):
    rid=Ride.objects.all()
    return render(request,'tableaux_C.html',{'rid':rid})

def addrid(request):
    x=request.POST['Pick']
    y=request.POST['Drop']
    z=request.POST['Price']
    rid=Ride(PickUpLocation=x,DropLocation=y,PriceMAD=z)
    rid.save()
    return render(request,'ridestatus.html',{'rid':rid})


def ridestatus(request,pk):
    ride = Ride.objects.get(pk=pk)
    return render(request,'ridestatus.html',{'rid':ride})
    

def accept_ride(request,pk):
    if request.method == 'POST':
        r = Ride.objects.get(pk=pk)
        r.status = 'Accepted'
        r.save()
        return redirect('tableaux_C')
    else:
        return redirect('tableaux_C')
def decline_ride(request,pk):
    if request.method == 'POST':
        r = Ride.objects.get(pk=pk)
        r.status = 'Declined'
        r.save()
        return redirect('tableaux_C')
    else:
        return redirect('tableaux_C')