from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('login', LoginView.as_view(), name='login'),
    path('register', UserCreateView.as_view(), name="register"),
    path('<int:pk>/deleteuser', UserDeleteView.as_view(), name='user_delete'),

    path('post', PostView.as_view(), name="post"),
    path('upload', PostWriteView.as_view(), name='upload'),
    path('<int:pk>/deletepost', PostDeleteView.as_view(), name='post_delete'),

    path('comments', CommentsView.as_view(), name="comments"),
    path('addcomments', CommentsWriteView.as_view(), name="addComments"),
    path('<int:pk>/deletecomment', CommentsDeleteView.as_view(), name='comment_delete'),
]
