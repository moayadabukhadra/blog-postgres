from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )

from blog.models import Article
from .serializers import ArticleSerializer
from blog.api.permissions import IsAuthenticatedOrReadOnly

class ArticlesListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class ArticlesDetailView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)