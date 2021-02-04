from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, filters
from .models import Post, Comment
from rest_framework.filters import SearchFilter

# 회원가입
class UserCreateView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# 로그인
class LoginView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    qs = super().get_queryset()
    return qs.filter(email=self.request.GET['email'], password=self.request.GET['password'])
    

# 유저 조회
class UserView(generics.ListAPIView):
  search_fields = ['id', 'username', 'email']
  filter_backends = (filters.SearchFilter, )
  queryset = User.objects.all()
  serializer_class = UserSerializer

# 유저 삭제
class UserDeleteView(generics.DestroyAPIView):
  queryset = User.objects.all()
  serializers_class = UserSerializer

# 게시글 가져오기
class PostView(generics.ListAPIView):
  search_fields = ['id', 'title', 'body', 'author']
  filter_backends = (filters.SearchFilter, )
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# 게시글 올리기
class PostWriteView(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# 게시글 삭제
class PostDeleteView(generics.DestroyAPIView):
  queryset = Post.objects.all()
  serializers_class = Post

# 코멘트 조회
class CommentsView(generics.ListAPIView):
  search_fields = ['post_id']
  filter_backends = (filters.SearchFilter, )
  queryset = Comment.objects.all()
  serializer_class = CommentsSerializer

# 코멘트 작성
class CommentsWriteView(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentsSerializer

  
# 게시글 삭제
class CommentsDeleteView(generics.DestroyAPIView):
  queryset = Comment.objects.all()
  serializers_class = Comment