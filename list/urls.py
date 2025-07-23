from django.urls import path


from . import views


urlpatterns = [
    path('', views.post_list, name='list'),
    path('users/<int:user_id>/', views.user_post_list, name='user_post_list'),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail")
]