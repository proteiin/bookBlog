from django.shortcuts import render, redirect
from .forms import myPostModelForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.
# @login_required
def create_Post(request):
    if request.user.is_authenticated :
        if request.method == "POST":
            form = myPostModelForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.time = timezone.now()
                post.save()
                return redirect('list') 
        else:
            form = myPostModelForm()
        return render(request,'post/index.html' , {"form":form})
    else:
        messages.error(request,"로그인 하고 이용하여 주십시오")
        return redirect('login')


