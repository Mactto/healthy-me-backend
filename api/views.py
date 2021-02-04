from .serializers import UserSerializer, PostSerializer, CommentsSerializer
from django.contrib.auth.models import User
from rest_framework import generics, filters
from .models import Post, Comment
from rest_framework.filters import SearchFilter

# 회원가입
class UserCreateView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# 유저 조회
class UserView(generics.ListAPIView):
  search_fields = ['id', 'username', 'email']
  filter_backends = (filters.SearchFilter, )
  queryset = User.objects.all()
  serializer_class = UserSerializer


# 게시글 가져오기
class PostView(generics.ListAPIView):
  search_fields = ['id', 'title', 'body', 'author']
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# 게시글 올리기
class PostWriteView(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# 코멘트 조회
class CommentsView(generics.ListAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentsSerializer

# 코멘트 작성
class CommentsWriteView(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentsSerializer