from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
    CreateView,
)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post


post_list = PostListView.as_view()


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("tube:post_list")
    template_name = "tube/form.html"


post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post


post_detail = PostDetailView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("tube:post_list")
    template_name = "tube/form.html"


post_edit = PostUpdateView.as_view()


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("tube:post_list")


post_delete = PostDeleteView.as_view()