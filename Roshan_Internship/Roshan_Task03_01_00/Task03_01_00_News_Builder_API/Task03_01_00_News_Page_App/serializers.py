from rest_framework import serializers
from .models import News, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name']

class NewsSerializer(serializers.ModelSerializer):
    news_tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'news_title', 'news_content', 'news_source', 'news_tags', 'news_created_at']