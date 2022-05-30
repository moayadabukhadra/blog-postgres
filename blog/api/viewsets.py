from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )

from rest_framework import generics 

from blog.models import Article
from .serializers import ArticleSerializer
from blog.api.permissions import IsAuthenticatedOrReadOnly



class ArticlesListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

   


class ArticlesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
