from django.urls import path
from django.views.generic import TemplateView

from posts import views

urlpatterns = [
    path(route="posts/<int:pk>/detail", view=views.PostDetailView.as_view(), name="detail"),
    path(route="posts/", view=views.PostsFeedView.as_view(), name="feed"),
    path(route="posts/new/", view=views.CreatePostView.as_view(), name="create_post"),
    path(route="posts/feactured", view=TemplateView.as_view(template_name="posts/feactured.html"), name="feactured")
]
