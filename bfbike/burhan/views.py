from django.shortcuts import render
from django.http import HttpResponse
from .models import off_road
from .models import On_road
import datetime


# Create your views here.
def main(request):
    return render(request,'front_page.html')
def Off_road(request):
    return render(request,'off_road.html')
def on_road(request):
    return render(request,'onroad.html')
def register(request):
    road="On Road"
    bike="NS-200"
    return render(request,'register.html',{'road':road,'bike':bike})
def mt15(request):
    road="On Road"
    bike="MT-15"
    return render(request,'register.html',{'road':road,'bike':bike})
def enfield350(request):
    road="On Road"
    bike="ROYAL ENFIELD 350 CLASSSIC"
    return render(request,'register.html',{'road':road,'bike':bike})
def apachertr(request):
    road="On Road"
    bike="APACHE RTR"
    return render(request,'register.html',{'road':road,'bike':bike})
def ktm390(request):
    road="On Road"
    bike="KTM 390"
    return render(request,'register.html',{'road':road,'bike':bike})
def yamahar15(request):
    road="On Road"
    bike="YAMAHA-R15"
    return render(request,'register.html',{'road':road,'bike':bike})

def himalyan(request):
    road="Off Road"
    bike="RE-HIMALAYAN"
    return render(request,'register2.html',{'road':road,'bike':bike})
def trk(request):
    road="Off Road"
    bike="BENELI-TRK-251"
    return render(request,'register2.html',{'road':road,'bike':bike})
def ktm(request):
    road="Off Road"
    bike="KTM-390"
    return render(request,'register2.html',{'road':road,'bike':bike})
def xpluse(request):
    road="Off Road"
    bike="HERO XPLUSE-200"
    return render(request,'register2.html',{'road':road,'bike':bike})
def bmw(request):
    road="Off Road"
    bike="BMW G 310 GS"
    return render(request,'register2.html',{'road':road,'bike':bike})
def yezdi(request):
    road="Off Road"
    bike="YEZDI"
    return render(request,'register2.html',{'road':road,'bike':bike})

def data1(request):
    if request.method=="POST":
        date=datetime.datetime.now()
        road="ON-ROAD"
        name=request.POST["name"]
        bike=request.POST["bike"]
        age=request.POST["age"]
        add1=request.POST["d_no"]
        add2=request.POST["s_name"]
        add3=request.POST["city"]
        add4=request.POST["district"]
        mob1=request.POST["mob1"]
        mob2=request.POST["mob2"]
        email=request.POST["email"]
        obj=On_road()
        obj.date=date
        obj.road=road
        obj.bike=bike
        obj.name=name
        obj.age=age
        obj.d_no=add1
        obj.s_name=add2
        obj.city=add3
        obj.dis=add4
        obj.mob1=mob1
        obj.mob2=mob2
        obj.email=email
        obj.save()
        return HttpResponse("Data added successfully, we will call back you sooon..")
    
    
def data2(request):
    if request.method=="POST":
        date=datetime.datetime.now()
        road="OFF-ROAD"
        name=request.POST["name"]
        bike=request.POST["bike"]
        age=request.POST["age"]
        add1=request.POST["d_no"]
        add2=request.POST["s_name"]
        add3=request.POST["city"]
        add4=request.POST["district"]
        mob1=request.POST["mob1"]
        mob2=request.POST["mob2"]
        email=request.POST["email"]
        obj1=off_road()
        obj1.date=date
        obj1.road=road
        obj1.bike=bike
        obj1.name=name
        obj1.age=age
        obj1.d_no=add1
        obj1.s_name=add2
        obj1.city=add3
        obj1.dis=add4
        obj1.mob1=mob1
        obj1.mob2=mob2
        obj1.email=email
        obj1.save()
        return HttpResponse("Data added successfully, we will call back you sooon..")
