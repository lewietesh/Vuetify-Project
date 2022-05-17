from django.urls import path


from blog import views

from rest_framework.urlpatterns import format_suffix_patterns

#define the urls




urlpatterns = [
    path('articles', views.PostsViewSet.as_view()),
    path('articles/<int:pk>', views.PostsDetail.as_view()),
    path("users", views.UserCreate.as_view(), name = "user_create"),
    path("login", views.LoginView.as_view(), name = "login")

]

