import feedparser
import requests


class DMHYRSSParser:
    def __init__(self, rss_url=None, proxy_url=None):
        self.items = None
        self.rss_url = rss_url if rss_url else 'https://share.dmhy.org/topics/rss/rss.xml'
        self.proxy_url = proxy_url

    @property
    def parse(self):
        proxies = None
        if self.proxy_url:
            proxies = {
                "http": self.proxy_url,
                "https": self.proxy_url
            }

        response = requests.get(self.rss_url, proxies=proxies)
        feed = feedparser.parse(response.content)

        items = []
        for item in feed.entries:
            data = {}
            data['title'] = item.title
            data['link'] = item.link
            data['description'] = item.description
            data['published'] = item.published
            data['category'] = item.category
            data['torrent_url'] = item.enclosures[0].href
            data['torrent_size'] = item.enclosures[0].length
            items.append(data)
        self.items = items
        return items


if __name__ == '__main__':
    dmhy_rss_parser = DMHYRSSParser(proxy_url='http://127.0.0.1:40900')
    print(dmhy_rss_parser.parse)
