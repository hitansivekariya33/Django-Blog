from django.urls import path
from .views import SignUp,SignIn,sign_out
urlpatterns = [
    path('',SignUp.as_view(),name='sign_up'),
    path('signin/',SignIn.as_view(),name='sign_in'),
    path('signout/',sign_out,name='sign_out')   
]