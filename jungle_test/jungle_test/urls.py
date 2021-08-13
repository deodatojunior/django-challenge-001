from django.urls import include, path
from rest_framework import routers
from .views import *
from knox import views as knox_views

urlpatterns = [
    path("api/admin/authors/", ListCreateAuthors.as_view()),
    path("api/admin/authors/<uuid:pk>/", DetailAuthors.as_view()),

    path("api/admin/articles/", ListCreateArticles.as_view()),
    path("api/admin/articles/<uuid:pk>/", DetailArticles.as_view()),
    path("api/articles/", GetByCategoryArticles.as_view()),

    path("api/articles/<uuid:id>/", GetByIdArticles.as_view()),

    path("api/sign-up/", SignUp.as_view()),
    path('api/login/', Login.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]

