from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request,user)
            return redirect("list")
        else:
            return render(request, "accounts/login.html", {"error":"로그인 실패"})
    return render(request,"accounts/login.html")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('list')
    else: 
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form':form} )

def logout_view(request):
    logout(request)
    return redirect('login')