# news_aggregator/models.py

from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50)
    cluster_label = models.IntegerField()
    source_rating = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'news_aggregator'
