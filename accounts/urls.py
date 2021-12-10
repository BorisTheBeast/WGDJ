from .views import RegisterAPI, UserAPI, LogoutAPI, ChangePasswordView
from rest_framework.authtoken import views
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/login/', views.obtain_auth_token, name='login'),
    path('api/logout/', LogoutAPI.as_view(), name='logout'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
