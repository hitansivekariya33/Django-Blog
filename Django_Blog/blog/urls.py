from django.urls import path
from .views import index,AuthorListView,AuthorDetailView,BlogListView,BlogDetailView,CommentFormView
urlpatterns = [
    path('',index.as_view(),name='index'),
    path('blogger/',AuthorListView.as_view(),name='authorlist'),
    path('blogger/<int:pk>/',AuthorDetailView.as_view(),name='authordetail'),
    path('blog/',BlogListView.as_view(),name='bloglist'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name='blogdetail'),
    path('blog/<int:pk>/create/',CommentFormView.as_view(),name='comment')
]
