from django.shortcuts import render
from details.models import Event

# Create your views here.
def fun1(request):
    result=Event.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        day=request.POST.get("date")
        place=request.POST.get("place")

        obj=Event(Name=name,Date=day,Venue=place)
        obj.save()
        result=Event.objects.all()
        return render(request,"insert.html",{"res":result , "obj":obj})
    return render(request,"insert.html")



def fun2(request):
    result=Event.objects.all()
    if request.method=="POST":
        Item=str(request.POST.get("name"))
        if Event.objects.filter(Name=Item).exists():
            abc=Event.objects.get(Name=Item) 
        else:
            abc=None
        return render(request,"record.html",{"res":result,"res2":abc})
    return render(request,"record.html")


def fun3(request):
    
    if request.method=="POST":

        name=request.POST.get("name")
        if Event.objects.filter(Name=name):
            result=Event.objects.all()
            abc=Event.objects.get(Name=name) 
            abc.delete()
        

   
            return render(request,"delete.html",{"result":result,"abc":abc})
    result=Event.objects.all()
    return render(request,"delete.html", {"result":result})





