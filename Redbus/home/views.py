from django.shortcuts import render,redirect
from .models import Journey
from .models import Travels
from .forms import JourneyForm
import json
# Create your views here.
def home(request):
    return render(request,'index.html')
def journey(request):
    

    if request.method=='POST':
        
        
        from_location=str(request.POST['from_location'])
        to_location=str(request.POST['to_location'])
        date=str(request.POST['date'])
        if to_location and from_location and date:
            j={'from_location':from_location,'to_location':to_location,'date':date}
            f=json.dumps(j)
        
            return render(request,'confirm.html',{'j':j,'f':f})
        else:
            return redirect('/')
    else:
        return redirect('index.html')

def edit(request,pk):
    trip = Journey.objects.get(pk=pk)
    
    form = JourneyForm(instance=trip)
    if request.method=='POST':
        form = JourneyForm(request.POST,instance=trip)
        if form.is_valid():
            form.save()
            
            
            msg=True
            note="Successfully Changed"
           
        else:
            msg=False
            note="Invalid"
        return render(request,'edit.html',{'note':note,'trip':trip ,'form':form,'msg':msg})
    else:

        return render(request,'edit.html',{'form':form,'trip':trip})

def confirm(request,f):
    
    g=json.loads(f)
    
    z=Journey(from_location=g["from_location"],to_location=g["to_location"],date=g["date"])
    z.save() 
    

    journey_pk=z.id
    travels=f
    c=Travels(journey_pk=journey_pk,travels=travels)
    c.save()
    
    return render(request,'confirm.html',{'journey_pk':journey_pk})

def delete(request,pk):
    ticket=Journey.objects.get(pk=pk)
    ticket.delete()
    return render(request,'delete.html')
def tickets(request):
    return render(request,'tickets.html')