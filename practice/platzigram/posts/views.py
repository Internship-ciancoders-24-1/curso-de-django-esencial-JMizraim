from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "post"
 
 
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = "posts"


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy("posts:feed")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context