from django_filters import rest_framework as filters
from .models import News
from django.db.models import Q

class NewsFilter(filters.FilterSet):
    tag = filters.CharFilter(field_name='news_tags__tag_name', lookup_expr='iexact')
    keyword_include = filters.CharFilter(method='filter_include_keywords')
    keyword_exclude = filters.CharFilter(method='filter_exclude_keywords')

    class Meta:
        model = News
        fields = ['tag']

    def filter_include_keywords(self, queryset, name, value):
        keywords_include_list = value.split(',')
        q = Q()
        for keyword_inc in keywords_include_list:
            q |= Q(news_content__icontains=keyword_inc) | Q(news_title__icontains=keyword_inc)
        return queryset.filter(q)

    def filter_exclude_keywords(self, queryset, name, value):
        keywords_exclude_list = value.split(',')
        for keyword_exc in keywords_exclude_list:
            queryset = queryset.exclude(
                Q(news_content__icontains=keyword_exc) | Q(news_title__icontains=keyword_exc)
            )
        return queryset