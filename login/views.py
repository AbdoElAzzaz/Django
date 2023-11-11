from django.shortcuts import render, redirect
from django.contrib import messages

# import model
from .models import users


# Create your views here.
def login_index(request):
    if request.POST:
        email = request.POST['email']
        real_email = users.objects.filter(email=email)
        if real_email:
            pwd = request.POST['pwd']
            real_pwd = users.objects.filter(pwd=pwd)
            if real_pwd:
                request.session['user'] = email
                return redirect("tasks_index")
            else:
                messages.warning(request, "Invalid password")
                return redirect("login_index")
        else:
            messages.warning(request, "Invalid Email")
            return redirect("login_index")
    else:
        return render(request, "login/index.html")