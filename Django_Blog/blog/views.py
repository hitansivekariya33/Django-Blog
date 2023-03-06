from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,CreateView,FormView
from .models import Author,Blog
from .form import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
# Create your views here.

class IndexView(TemplateView):
    template_name = "base.html"

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
        
class BlogListView(ListView):
    model = Blog
    paginate_by = 5   

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

class CommentView(LoginRequiredMixin, FormView):
    login_url = 'sign_in'
    def get(self, request, pk):
        blog = Blog.objects.filter(pk=pk).first()
        form = CommentForm()
        context = {
            'blog': blog,
            'form': form,
        }
        return render(request, 'blog/comment_form.html', context)

    def post(self, request, pk):
        blog = Blog.objects.filter(pk=pk).first()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog.pk
            comment.save()
            return redirect(comment.blog.get_absolute_url())

        context = {
            'blog': blog,
            'form': form,
        }
        return render(request, 'blog/comment_form.html', context)

class AuthorForm(CreateView):
    model = Author
    fields = ['name','about_author']
    success_url = '/blog/blogger/'

class BlogForm(CreateView):
    model = Blog
    fields = ['author','title','blog_content']
    success_url = '/blog/blogs/'