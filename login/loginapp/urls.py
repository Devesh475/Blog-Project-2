from django.urls import path
from . import views


urlpatterns = [
    path('<str:slug>/',views.blog_post_detail_view,name="blog_post_detail_view"),
    path('<str:slug>/comments',views.addComment,name="addComment"),
    path('',views.blog_post_list_view,name="blog_post_list_view"),
    path('<str:slug>/edit/',views.blog_post_update_view,name="blog_post_update_view"),
    path('<str:slug>/delete/',views.blog_post_delete_view,name="blog_post_delete_view"),
]