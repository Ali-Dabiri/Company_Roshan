from django.test import TestCase
from .models import News, Tag
from rest_framework.test import APIClient

class NewsListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        tag1 = Tag.objects.create(tag_name='tech')
        tag2 = Tag.objects.create(tag_name='gold')
        news1 = News.objects.create(news_title='Test News 1', news_content='This is test content 1', news_source='Source A')
        news2 = News.objects.create(news_title='Test News 2', news_content='This is test content 2', news_source='Source B')
        news1.news_tags.add(tag1)
        news2.news_tags.add(tag2)

    def test_get_list_all_news(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_tag(self):
        response = self.client.get('/api/news/?tag=tech')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['news_title'], "Test News 1")

    def test_filter_keyword_include(self):
        response = self.client.get('/api/news/?keyword_include=This')
        self.assertEqual(len(response.data), 2)
        self.assertIn(response.data[1]["news_source"], ["Source A", "Source B"])

    def test_filter_keyword_exclude(self):
        response = self.client.get('/api/news/?keyword_exclude=content 1')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["news_title"], "Test News 2")

    def test_filter_keyword_include_and_keyword_exclude(self):
        response = self.client.get("/api/news/?keyword_include=content 1&keyword_exclude=content 2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["news_title"], "Test News 1") 