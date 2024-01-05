from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Task
# Create your views here.
def home(request):
    context =  {'success' : False,'name':'Sam'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins =  Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context =  {'success' : True,'name':'Sam'}


    return render(request, 'index.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    for item in allTasks:
        print(item.taskTitle)
    context = { 'tasks': allTasks}
    return render(request, 'tasks.html', context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request, "hey hey")

        return redirect('tasks')
        
    return render(request, 'signup.html')

def land(request):
    return render(request,'land.html')
    
def pdf(request):
    return render(request, 'pdf.html')

def contact(request):
    return render(request, 'contact.html')



