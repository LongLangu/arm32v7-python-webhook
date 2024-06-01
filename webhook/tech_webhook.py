from datetime import datetime

from .base_webhook import ProdDiscordWebhook


class TechTrendWebhook(ProdDiscordWebhook):
    
    def __init__(self):
        super().__init__()
        self.parser('https://yamadashy.github.io/tech-blog-rss-feed/feeds/rss.xml')

    def show(self, num):
        content = {
            "username": "Tech",
            "embeds": [{
                "title": self.r[num]['title'],
                "description": self.r[num]['summary'],
                "url": self.r[num]['link'],
                "image": {
                    "url": self.r[num]['links'][1]['href']
                },
                "timestamp":self.convert_datetime(self.r[num]['published']),
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')
        r_today = [ r for r in self.r if self.is_within_24_hours(r['published'])]
        content = {
            "username": "Tech",
            "embeds": [{
                "title": f"{today_str}のトレンド記事",
                "fields": [{"name":f"{i+1}の記事", "value":"[{}]({})".format(r['title'], r['link']), "inline": True} for i, r in enumerate(r_today) if i < 25]
            }]
        }
        return self.discord_webhook(content)

class QiitaTrendWebhook(ProdDiscordWebhook):
    def __init__(self):
        super().__init__()
        self.parser('https://qiita.com/popular-items/feed')

    def show(self, num):
        content = {
            "username": "Qiita",
            "avatar_url": "https://github.com/qiita.png",
            "embeds": [{
                "title": self.r[num]['title'],
                "description": self.r[num]['summary'],
                "url": self.r[num]['link'],
                "timestamp":self.r[num]['published'],
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')

        r_today = [ r for r in self.r if self.is_within_24_hours_iso_8601(r['published'])]
        content = {
            "username": "Qiita",
            "avatar_url": "https://github.com/qiita.png",
            "embeds": [{
                "title": f"{today_str}のトレンド記事",
                "fields": [{"name":f"{i+1}の記事", "value":"[{}]({})".format(r['title'], r['link']), "inline": True} for i, r in enumerate(r_today) if i < 25]
            }]
        }
        return self.discord_webhook(content)

class QiitaTopicWebhook(ProdDiscordWebhook):
    def __init__(self, topic):
        super().__init__()
        self.topic = topic
        self.parser(f'https://qiita.com/tags/{topic}/feed')

    def show(self, num):
        content = {
            "username": "Qiita",
            "avatar_url": "https://github.com/qiita.png",
            "embeds": [{
                "title": self.r[num]['title'],
                "description": self.r[num]['summary'],
                "url": self.r[num]['link'],
                "timestamp":self.r[num]['published'],
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')

        r_today = [ r for r in self.r if self.is_within_24_hours_iso_8601(r['published'])]
        content = {
            "username": "Qiita",
            "avatar_url": "https://github.com/qiita.png",
            "embeds": [{
                "title": f"{today_str}の{self.topic}の記事",
                "fields": [{"name":f"{i+1}の記事", "value":"[{}]({})".format(r['title'], r['link']), "inline": True} for i, r in enumerate(r_today) if i < 25]
            }]
        }
        return self.discord_webhook(content)

class ZennTrendWebhook(ProdDiscordWebhook):

    def __init__(self):
        super().__init__()
        self.parser('https://zenn.dev/feed')

    def show(self, num):
        content = {
            "username": "Zenn",
            "avatar_url": "https://github.com/zenn-dev.png",
            "embeds": [{
                "title": self.r[num]['title'],
                "description": self.r[num]['summary'],
                "url": self.r[num]['link'],
                "image": {
                    "url": self.r[num]['links'][1]['href']
                },
                "timestamp":self.convert_datetime(self.r[num]['published']),
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')

        r_today = [ r for r in self.r if self.is_within_24_hours(r['published'])]
        
        content = {
            "username": "Zenn",
            "avatar_url": "https://github.com/zenn-dev.png",
            "embeds": [{
                "title": f"{today_str}のトレンド記事",
                "fields": [{"name":f"{i+1}の記事", "value":"[{}]({})".format(r['title'], r['link']), "inline": True} for i, r in enumerate(r_today)]
            }]
        }
        return self.discord_webhook(content)
    
class ZennTopicWebhook(ProdDiscordWebhook):
    
    def __init__(self, topic):
        super().__init__()
        self.topic = topic
        self.parser(f'https://zenn.dev/topics/{self.topic}/feed?all=1')

    def show(self, num):
        content = {
            "username": "Zenn",
            "avatar_url": "https://github.com/zenn-dev.png",
            "embeds": [{
                "title": self.r[num]['title'],
                "description": self.r[num]['summary'],
                "url": self.r[num]['link'],
                "image": {
                    "url": self.r[num]['links'][1]['href']
                },
                "timestamp":self.convert_datetime(self.r[num]['published']),
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')

        r_today = [ r for r in self.r if self.is_within_24_hours(r['published'])]

        content = {
            "username": "Zenn",
            "avatar_url": "https://github.com/zenn-dev.png",
            "embeds": [{
                "title": f"{today_str}の{self.topic}の記事",
                "fields": [{"name":f"{i+1}の記事", "value":"[{}]({})".format(r['title'], r['link']), "inline": True} for i, r in enumerate(r_today)]
            }]
        }
        return self.discord_webhook(content)

class ArxivWebhook(ProdDiscordWebhook):

    def __init__(self, category):
        super().__init__()
        self.category = category
        self.parser_arxiv(category)

    def show(self, num):
        content = {
            "username": "Arxiv",
            "embeds": [{
                "title": self.r[num].title,
                "summa": self.r[num].summary,
                "url": self.r[num].entry_id,
            }]
        }
        return self.discord_webhook(content)

    def lists(self):
        today = datetime.now()

        # 日付を YYYY-MM-DD 形式の文字列にフォーマット
        today_str = today.strftime('%Y年%m月%d日')
        content = {
            "username": "Arxiv",
            "embeds": [{
                "title": f"{today_str}の論文",
                "fields": [{"name":f"{i+1}の論文", "value":"[{}]({})".format(r.title, r.entry_id), "inline": True} for i, r in enumerate(self.r)]
            }]
        }
        return self.discord_webhook(content)