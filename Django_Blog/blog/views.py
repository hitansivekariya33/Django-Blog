from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .form import CommentForm
from .models import Author,Blog
# Create your views here.

class index(TemplateView):
    template_name = "base.html"

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(author=self.object)
        return context

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html' 
    paginate_by = 5   

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

class CommentFormView(CreateView):
    form_class = CommentForm
    template_name = 'Comment_Form.html'