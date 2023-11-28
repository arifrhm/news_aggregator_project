# news_aggregator/utils/rss.py

import feedparser

def fetch_rss_feed(url):
    try:
        feed = feedparser.parse(url)

        if hasattr(feed, 'entries'):
            entries = feed.entries

            for entry in entries:
                # Extracting the image URL from the content or description
                content = entry.get('content', '')
                description = entry.get('description', '')
                image_url = content[0].get('value') if content else description.split('<img')[1].split('src="')[1].split('"')[0] if '<img' in description else ''

                entry['image_url'] = image_url

            return entries
        else:
            return []
    except Exception as e:
        print(f"Error fetching or parsing the feed: {e}")
        return []

# Example usage:
rss_feed_url = 'https://www.antaranews.com/rss/terkini.xml'
articles = fetch_rss_feed(rss_feed_url)

for idx, article in enumerate(articles, 1):
    print(f"\nArticle {idx}:")
    print(f"Title: {article.get('title', 'No Title')}")
    print(f"Link: {article.get('link', 'No Link')}")
    print(f"Publication Date: {article.get('published_parsed', 'No Date')}")
    print(f"Description: {article.get('summary', 'No Summary')}")
    print(f"Image URL: {article.get('image_url', 'No Image')}")
