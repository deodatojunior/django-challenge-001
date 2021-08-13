from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import generics, permissions, views
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import *
from .models import *

from .serializers import UserSerializer, SignUpSerializer


class SignUp(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class Login(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(Login, self).post(request, format=None)


class ListCreateAuthors(views.APIView):
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetailAuthors(views.APIView):
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreateArticles(views.APIView):
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        authors = Article.objects.all()
        serializer = ArticleSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetailArticles(views.APIView):
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCategoryBySlugArticles(views.APIView):
    serializer_class = ArticleSlugSerializer

    def get(self, request, format=None):
        cat = request.GET.get('category', "")
        cat = str(cat)
        articles = Article.objects.filter(category__exact=cat)
        serializer = ArticleSlugSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetCategoryByIdArticles(views.APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, id,  format=None):
        article = Article.objects.filter(id__exact=id)
        if request.user.is_anonymous:
            serializer = ArticleAnonymousSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.user.is_authenticated:
            serializer = ArticleLoggedSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



