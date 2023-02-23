from django.urls import path
from .views import Sign_up,Sign_in,sign_out
urlpatterns = [
    path('',Sign_up.as_view(),name='sign_up'),
    path('signin/',Sign_in.as_view(),name='sign_in'),
    path('signout/',sign_out,name='sign_out')   
]