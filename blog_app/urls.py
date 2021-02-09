from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # here name attribute value is post_list which means it will take you to post_list page.
]