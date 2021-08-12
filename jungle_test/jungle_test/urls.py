from django.urls import include, path
from rest_framework import routers
from .views import *
from knox import views as knox_views

urlpatterns = [
    path("api/admin/author/", ListCreateAuthors.as_view()),
    path("api/admin/author/<uuid:pk>/", DetailAuthors.as_view()),
    path("api/admin/article/", ListCreateArticles.as_view()),
    path("api/admin/article/<uuid:pk>/", DetailArticles.as_view()),
    path("api/sign-up/", SignUp.as_view()),
    path('api/login/', Login.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]

