from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view(), name='user_list_create'),

]
