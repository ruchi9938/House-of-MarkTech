from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "tasks/login.html")

@login_required
def dashboard(request):
    return render(request, "tasks/dashboard.html")

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

@login_required  # Ensure only logged-in users can create tasks
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet
            task.user = request.user        # Assign the logged-in user
            task.save()                     # Now save the task
            return redirect("task-list")
    else:
        form = TaskForm()
    
    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.status = request.POST.get("status", task.status)
        task.priority = request.POST.get("priority", task.priority)
        task.save()
        return redirect("task_detail", task_id=task.id)

    return render(request, "tasks/task_detail.html", {"task": task})