from django.shortcuts import render
from django.views.generic.base import TemplateView

class PostView(TemplateView):
    template_name = 'forum/posts.html'

class PostDetailView(TemplateView):
    template_name = 'forum/post.html'