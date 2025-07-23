from django.shortcuts import render, redirect, get_object_or_404
from post.models import PostModel
from accounts.models import CustomUser

from post.models import PostModel
from comments.forms import commentsForm
from comments.models import CommentsModel

def post_list(request):
    posts = PostModel.objects.all()
    return render(request, 'list/posting_list.html', {'posts': posts})


# Create your views here.

def user_post_list(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts= PostModel.objects.filter(author =user)
    return render(request, 'list/user_post.html',{
                      'user':user,
                      'posts':posts}
                  )

def post_detail(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    comments = CommentsModel.objects.filter(post=post).order_by('-time')
    

    if request.method =="POST":
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = commentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.post = post
            comments.author = request.user
            comments.save()

    else:
        form = commentsForm()
    return render(request, 'list/post_detail.html' , {
        'post': post, 'comments':comments, 'form':form})

        

    # #else if request.method == "Patch":

    # else if request.method == "Delete":

    # else:
    #     form = commentsForm
    
    
