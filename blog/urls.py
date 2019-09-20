from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.post_list, name ="index"),
     path('post/<int:pk>/', views.post_detail, name="post_detail"),
     path('new/',views.post_new, name ="post_new"),
     path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
]


