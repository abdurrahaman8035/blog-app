from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    """Display list of BlogPosts to the User"""

    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_post_list'

class BlogDetailView(DetailView):
    """Display the contents of a particular blog post"""

    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    """Create a new blog post"""

    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    """Edit a blog post"""

    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    """Delete a bolg post"""

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
