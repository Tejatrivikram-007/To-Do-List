from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name=(request.POST['name'])
            desc=(request.POST['desc'])
            user=request.user     #this will fetch the current authenticated
            Task.objects.create(name=name,description=desc,user=user)
            return redirect('home')

        all_task=Task.objects.filter(user=request.user)
        context={
            'all_tasks':all_task
        }
        return render(request, 'home.html',context)
    else:
        return redirect('login')

    

def update_task(request,pk):
    try:
        task=Task.objects.get(id=pk,user=request.user)
    except:
        return HttpResponse(f'The Task with id= {pk} does not exist')
        
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        task.name = name
        task.description=desc
        task.save()
        return redirect('home')

    context={
        'task':task
    }
    return render(request,'update.html',context)

def delete_task(request,pk):
    try:
        task=Task.objects.get(id=pk,user=request.user)
    except:
        return HttpResponse(f'The Task with id= {pk} does not exist')
    task.delete()
    return redirect('home')
    