from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=="POST":
        sap = request.POST['sap']
        ledger = request.POST['ledger']
        manufacture = request.POST['manufacture']
        model = request.POST['model']
        vehicletype = request.POST['vehicletype']
        basekm = request.POST['basekm']
        rto = request.POST['rto']
        modelyear = request.POST['modelyear']
        chassisno = request.POST['chassis']
        fuel = request.POST['fuel']
        oldvehicleno = request.POST['oldvehichle']
        obj = engine(sap=sap,ledger=ledger,manufacture=manufacture,model=model,
                     vehicle_type=vehicletype,base_km=basekm,rto=rto,model_year=modelyear,
                     chassis=chassisno,fuel_type=fuel,old_vehicle=oldvehicleno)
        obj.save()
        messages.success(request,'Form Submitted Successfully !!')
        return redirect('/')

    return render(request,"index.html")