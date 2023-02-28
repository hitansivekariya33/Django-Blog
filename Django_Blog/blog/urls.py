from django.urls import path
from .views import IndexView,AuthorListView,AuthorDetailView,BlogListView,BlogDetailView,commentview
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('blogger/',AuthorListView.as_view(),name='authorlist'),
    path('blogger/<int:pk>/',AuthorDetailView.as_view(),name='authordetail'),
    path('blogs/',BlogListView.as_view(),name='bloglist'),
    path('blogs/<int:pk>/',BlogDetailView.as_view(),name='blogdetail'),
    path('blogs/<int:pk>/create/',commentview,name='comment'),
]
