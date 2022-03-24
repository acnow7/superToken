from django.urls import path
from .views.user import SignUp, SignIn, SignOut, ChangePasswordView
from .views.blog import BlogsView, BlogView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('update-password/', ChangePasswordView.as_view(), name='update-password'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>', BlogView.as_view(), name='my-blogs'),
]