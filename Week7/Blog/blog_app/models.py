from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    written = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text