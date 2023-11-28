# news_aggregator/views.py

from django.shortcuts import render
from .models import NewsArticle
from .management.commands.fetch_news import Command
def index(request):
    # Fetch news articles from the Wall Street Journal RSS feed
    # Create an instance of the Command class
    fetch_command = Command()
    # Call the handle method on the instance
    fetch_command.handle()
    articles = NewsArticle.objects.all()
    context = {'articles': articles}
    return render(request, 'news_aggregator/index.html', context)