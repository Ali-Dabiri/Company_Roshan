from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name

class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_content = models.TextField()
    news_source = models.CharField(max_length=255)
    news_tags = models.ManyToManyField(Tag, related_name='news')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title