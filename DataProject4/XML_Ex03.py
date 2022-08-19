"""
https://rss.hankyung.com/feed/headline.xml 의  뉴스를 읽어서 출력하시오
"""

import feedparser

news_list = feedparser.parse("https://rss.hankyung.com/feed/headline.xml")
print(news_list.entries[0] )

for news in news_list.entries:
    # print(news)
    print(news['title'])
    # print(news['title_detail']['value'])
    # print(news['title_detail']['base'])
    print(news['link'])
    print("-" * 80)