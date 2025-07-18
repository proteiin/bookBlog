from django.shortcuts import render, get_object_or_404
from post.models import PostModel
from accounts.models import CustomUser


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