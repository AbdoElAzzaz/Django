from django.shortcuts import render, redirect
from django.contrib import messages

# models
from login.models import users


# Create your views here.
def register_index(request):
    if request.POST:
        # user data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['pwd']

        # databases insert
        new_user = users()
        is_email = users.objects.filter(email=email)
        if is_email:
            messages.warning(request, "This email is already exist! try to login")
            return redirect("login_index")
        else:
            new_user.username = first_name + "_" + last_name
            new_user.email = email
            new_user.pwd = pwd
            new_user.save()
            messages.success(request, "you have successfully create new account!")
            return redirect("login_index")
    else:
        return render(request, "register/index.html")