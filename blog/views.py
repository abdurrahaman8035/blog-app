# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """Display list of BlogPosts to the User"""

    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_post_list'

class BlogDetailView(DetailView):
    """Display the contents of a particular blog post"""

    model = Post
    template_name = 'post_detail.html'
    