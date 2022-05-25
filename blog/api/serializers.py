from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = ('title','date_created','updated' ,'author', 'content', 'published')