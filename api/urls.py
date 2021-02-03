from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('register', UserView.as_view(), name="register"),
    path('post', PostView.as_view(), name="post"),
    path('upload', PostWriteView.as_view(), name='upload'),
    path('comments', CommentsView.as_view(), name="comments"),
    path('addcomments', CommentsWriteView.as_view(), name="addComments")
]