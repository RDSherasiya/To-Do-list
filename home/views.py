from django.shortcuts import redirect, render
from home.models import Task
# Create your views here.
def home(request):
     context = {'success': False}
     if request.method == "POST":
        #Handle the form 
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
        
    
     return render (request,'index.html',context)
    
def tasks(request):
     allTasks = Task.objects.all()  # this will fetch all the tasks from the database 
     # print(allTasks)
     # for item in allTasks:
     # print(item.taskTitle)
     context = {'tasks': allTasks} # this 'tasks' variable contains all the tasks which is written by the task.bojects.all() 

     return render(request,'tasks.html', context)

    
def delete(request,id):
    obj = Task.objects.get(id=id)
    obj.delete()
    return redirect('tasks')