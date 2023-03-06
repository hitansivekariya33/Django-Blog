from django.urls import path
from .views import (
    IndexView,
    AuthorListView,
    AuthorDetailView,
    BlogListView,
    BlogDetailView,
    CommentView,
    AuthorForm,
    BlogForm,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("blogger/", AuthorListView.as_view(), name="authorlist"),
    path("blogger/<int:pk>/", AuthorDetailView.as_view(), name="authordetail"),
    path("blogger/form/", AuthorForm.as_view(), name="authorform"),
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blogdetail"),
    path("blogs/<int:pk>/create/", CommentView.as_view(), name="comment"),
    path("blogs/form/", BlogForm.as_view(), name="blogform"),
]
