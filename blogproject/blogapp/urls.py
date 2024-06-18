from django.urls import path
from .views import Home
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', Home.as_view()),
   
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    #Profile
    path('profile/', views.getProfile, name='profile'),
    path('profile/update/', views.updateProfile, name='update-profile'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #blogs
    path('blogs/', views.getBlogs, name="blogs"),
    path('blogs/<int:pk>/', views.getBlog, name="blog"),
    path('blogs/create/', views.createBlog, name="create-blog"),
    path('blogs/<int:pk>/update/', views.updateBlog, name="update-blog"),
    path('blogs/<int:pk>/delete/', views.deleteBlog, name="delete-blog"),
    path('users/<int:pk>/blogs',views.getUserBlogs, name="my-blogs"),
    path('blogs/create/', views.createBlog, name="create-blog"),


]