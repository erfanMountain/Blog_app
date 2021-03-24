from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # here name attribute value is post_list which means it will take you to post_list page.
    #127.0.0.1#8082/post/1 SO that pk means it will go to that specific post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # when it is 127.0.0.1:8000/post/new --> local
    # when it is mydjangosite.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),

    #127.0.0.1:8000/post/2/edit --> local
    # mydjangosite.com/post/2/edit --> online
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),

    #127.0.0.1:8000/drafts --> local
    # mydjangosite.com/drafts --> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    #127.0.0.1:8000/post/2/publish --> local
    # mydjangosite.com/post/2/publish --> online
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish')
]