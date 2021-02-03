from django.urls import path
from .views import UserView
from .views import UserCreateView

app_name = 'api'
urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('register', UserCreateView.as_view(), name="register"),
    #path('hello/', HelloView.as_view(), name='hello'),
]