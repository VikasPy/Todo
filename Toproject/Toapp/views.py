from django.shortcuts import render,redirect
from .form import*
from .models import*
# Create your views here.

def base(request):
    return render(request,'base.html')


def todo(request):
    if request.method == 'GET':
            sd= todo_box.objects.all()
            s=todo_for()
            return render(request,'todo.html',{'s':s,'sd':sd})
    else:
        d=todo_for(request.POST)
        if d.is_valid():
            d.save()
            return redirect('todo')
        else:
            return render(request,'todo.html')
        
        
        
def update(request,id):
    try:
        data= todo_box.objects.get(id=id)
        print(data)
    except Exception as e:
        print(e)
    
    if request.method == 'GET':
            sd= todo_box.objects.all()
            s=todo_for(instance=data)
            return render(request,'todo.html',{'s':s,'sd':sd})
        
    else:
        sda=todo_for(request.POST,instance=data)
        # if sda.is_valid():
        sda.save()
        return redirect("todo")

        
        
            
            
        
        
def delete(request,id):
    d=todo_box.objects.get(id=id)
    d.delete()
    return redirect("todo")
