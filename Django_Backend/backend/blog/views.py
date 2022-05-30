

from .models import Posts
from rest_framework import generics
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from .serializers import PostsSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
# Create your views here.


class PostsViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Posts.objects.all().order_by('-date_published')
    serializer_class = PostsSerializer

    def destroy(self, request, *args, **kwargs):
        article = Posts.objects.get(pk=self.kwargs["pk"])

        if not request.user == article.created_by:
            raise PermissionDenied("You cannot delete this article")
        return super() .destroy(request, *args, **kwargs)


class PostsDetail (generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class UserCreate(generics.CreateAPIView):
    # these two are to exempt UserCreate from global authenthication scheme
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

# for creating authenthication token on creating a new user


class LoginView(generics.CreateAPIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return JsonResponse({
                "token": user.auth_token.key,
                'isAuthenticated': True,
                'title': "Login Successful",
                'message': "You have been logged in successfully",
                'username': user.username,
                'email': user.email,

            })
        else:
            return JsonResponse({
                "title": "Invalid credentials",
                "isAuthenticated": False,
                'message': "The username or password you input is incorrect try again"

            },
                status=201)

# FUNCTION BASED VIEWS APPROACH WHICH IS QUITE FLEXIBLE AND CUSTOMIZABLE

# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, id):
#     try:

#         article = Posts.objects.get(id = id)

#         data = {
#             "results": {
#                 'id': article.id,
#                 'title': article.title,
#                 'category': article.category,
#                 'content': article.content,
#                 'image': article.image,
#                 'date_published': article.date_published,
#                 'author': article.author,
#                 'comments': article.comments,
#                 'likes': article.likes
#             }
#         }
#         return JsonResponse(data)
#     except Posts.DoesNotExist:
#         return JsonResponse({
#             'message': "This article does not exist"
#         })
