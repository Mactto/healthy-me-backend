from django.urls import path
from .views import UserRecordView
from .views import HelloView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('hello/', HelloView.as_view(), name='hello'),
]