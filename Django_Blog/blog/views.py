from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from .models import Author,Blog
from .form import CommentForm
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='sign_in')
def commentview(request,pk):
    blog = Blog.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            object = form.save(commit=False)
            object.blog_id = blog.pk
            object.save()
            return redirect(object.blog.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'blog' : blog,
        'form' : form,
    }            
    return render(request,'blog/comment_form.html',context)