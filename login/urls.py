from django.urls import path
from .views import UserRegisterView, UserLoginView, AdminLoginView

urlpatterns = [
    path('user/signup/', UserRegisterView.as_view(), name='user-register'),
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
]