from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    # Here we use the cascade this is because if we delete the autor it will also delete all the comments.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # reason why we created the publish function this is because some time we write the post but we don't post it when we will finally post then It will call this function.

    def approved_comments(self):
        return self.comments.filter(approved=True)


    # create a string representation
    def __str__(self):
        return self.title


# Creating the table for comments
class Comment(models.Model):
    """
    Here we use the cascade this is because if we delete the post it will also delete all the comments.
    Post.objects.get(pk=2).comments.all()
    """

    post = models.ForeignKey('blog_app.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        """
            It will return the text
        """
        return self.text
