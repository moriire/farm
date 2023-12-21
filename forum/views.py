from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class PostView(LoginRequiredMixin, TemplateView):
    template_name = 'forum/posts.html'

class PostDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'forum/post.html'