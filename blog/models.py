from django.db import models
from django.urls import reverse


class Post(models.Model):
    """A simple model representing a blog post"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        """String to represent post"""

        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
