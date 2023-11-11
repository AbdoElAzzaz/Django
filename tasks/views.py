from django.shortcuts import render, redirect
from django.contrib import messages

# import models
from tasks.models import tasks


# Create your views here.
def tasks_index(request):
    if request.POST:
        # user data
        task_name = request.POST['task']
        date = "22-09-2022"
        stat = 0
        email = request.session['user']
        # data init
        new_task = tasks()
        new_task.task_name = task_name
        new_task.email = email
        new_task.stat = stat
        new_task.date = date
        new_task.save()
        return redirect("tasks_index")
    else:
        if "user" in request.session:
            email = request.session['user']
            all_tasks = tasks.objects.filter(email=email)
            return render(request, "tasks/index.html", {"tasks": all_tasks})
        else:
            messages.warning(request, "You should login first!")
            return redirect("login_index")


def logout(request):
    del request.session['user']
    return redirect("login_index")

def delete(request,id):
    item = tasks.objects.get(id=id)
    item.delete()
    return redirect('tasks_index')

def done(request,id):
    item = tasks.objects.get(id=id)
    item.stat = 1
    item.save()
    return redirect('tasks_index')
