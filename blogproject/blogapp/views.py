from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser, Blog
from api.serializer import BlogSerializer, ProfileSerializer, MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer




@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/',
        'api/blogs/',
        'api/blog/<int:pk>/',
        'api/blog/<int:pk>/update/',
        'api/blog/<int:pk>/delete/',
        'api/blog/myblogs/',
        'api/blog/create/',
        'api/profile/',
        'api/profile/update/',
        'api/users/<int:pk>/notes',

    ]
    return Response(routes)


#blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogs(request):
    public_blogs = Blog.objects.filter(is_public=True).order_by('-updated')[:10]
    user_blogs = request.user.blogs.all().order_by('-updated')[:10]
    blogs= public_blogs | user_blogs
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


#blogs/<int:pk>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlog(request, pk):
    blog = request.user.blogs.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


#blogs/<int:pk>/update
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateBlog(request, pk):
    blog = request.user.blogs.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#blogs/<int:pk>/delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBlog(request, pk):
    note = request.user.blogs.get(id=pk)
    note.delete()
    return Response('Note was deleted')


#blogs/create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBlog(request):
    user = request.user
    data = request.data
    blog = Blog.objects.create(
           user=user,
        title=data['title'],
        body=data['body'],
    )
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

#blogs/user/<int:pk>/myblogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserBlogs(request, pk):
    user = CustomUser.objects.get(id=pk)
    blogs = Blog.objects.filter(user=user)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


#profile  and profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




