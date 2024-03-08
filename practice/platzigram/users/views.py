from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from users.forms import SignupForm
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from posts.models import Post
from users.models import Profile


# from django.db.utils import IntegrityError
class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    # queryset = User.objects.all()
    model = User
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        # es el encargado de hacer la consulta a la bd
        return context 

class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = "users/login.html"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/update_profile.html"
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    
    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self) -> str:
        username = self.object.user.username
        return reverse('users:detail', kwargs={
            'username': username
        })