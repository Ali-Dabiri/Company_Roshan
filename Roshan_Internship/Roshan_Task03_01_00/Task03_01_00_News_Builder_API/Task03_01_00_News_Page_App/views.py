from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import News
from .serializers import NewsSerializer
from .filters import NewsFilter

class NewsListAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all().prefetch_related('news_tags').order_by('-news_created_at')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter