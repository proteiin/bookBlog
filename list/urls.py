from django.urls import path

from . import views


urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:user_id>/', views.user_post_list, name='user_post_list')
]