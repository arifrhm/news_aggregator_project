# news_aggregator/management/commands/fetch_news.py

import datetime
from django.core.management.base import BaseCommand
from news_aggregator.utils.rss import fetch_rss_feed
from news_aggregator.models import NewsArticle

class Command(BaseCommand):
    help = 'Fetch news articles from a sample RSS feed and update the database'

    def handle(self, *args, **kwargs):
        # Sample RSS feed URL
        rss_feed_url = 'https://www.antaranews.com/rss/terkini.xml' #Antara NEWS
        
        # Fetch articles from the RSS feed
        articles = fetch_rss_feed(rss_feed_url)

        # Save fetched articles to the database
        for article in articles:
            title = article.get('title', 'No Title')
            content = article.get('summary', 'No Content')
            pub_date = article.get('published_parsed', None)

            if pub_date:
                pub_date = datetime.datetime(*pub_date[:6])

            # Create or update the NewsArticle model
            news_article, created = NewsArticle.objects.update_or_create(
                title=title,
                defaults={
                    'content': content,
                    'pub_date': pub_date,
                    'category': 'Uncategorized',  # You may update this based on your categorization
                    'cluster_label': 0,  # You may update this based on your clustering
                    'source_rating': 0.0,  # You may update this based on your rating system
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added article: {title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Article already exists: {title}'))
