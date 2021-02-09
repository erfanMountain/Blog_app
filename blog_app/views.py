from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend) #stuff_for_frontend here is the context dictionary

def post_detail(request, pk):
    # we put the primary key in here this is because we can go for sepecific posts with their comments
    post = get_object_or_404(Post, pk=pk) # it will get either specific posts or throw the 404
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)
