import json
import os
from datetime import datetime, timedelta

import arxiv
import feedparser
import requests
from dateutil import parser

from webhook.config import Development, Production, Test

envs = {
    'development': Development,
    'test': Test,
    'production': Production,
}


class ProdDiscordWebhook(object):

    def __init__(self):

        self.env = envs[os.environ.get('ENVIRONMENT', 'development')]()
        print(self.env)
        self.discord_webhook_url = self.env.get_webhook_url()

    
    def is_within_24_hours(self, date_string):
        date_obj = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S GMT')
        now = datetime.now()
        difference = now - date_obj
        return difference <= timedelta(hours=24)

    def is_within_24_hours_iso_8601(self, date_string):
        date_obj = parser.isoparse(date_string)
        now = datetime.now(date_obj.tzinfo)
        difference = now - date_obj
        return difference <= timedelta(hours=24)

    def convert_datetime(self, original_datetime_str):
        # 元の日時の形式
        original_format = '%a, %d %b %Y %H:%M:%S GMT'
        # 日時文字列をdatetimeオブジェクトに変換（UTCを基準として）
        original_datetime = datetime.strptime(original_datetime_str, original_format)
        # JSTに変換（UTCから+9時間）
        jst_datetime = original_datetime + timedelta(hours=9)
        # 新しい形式の日時文字列に変換
        new_datetime_str = jst_datetime.strftime('%Y-%m-%dT%H:%M:%S+09:00')

        return new_datetime_str

    def get_current_and_last_week(self, ):

        now = datetime.now()
        current_weekday = now.weekday()

        last_monday = now - timedelta(days=current_weekday + 7)
        last_monday_start = last_monday.replace(hour=0, minute=0, second=0, microsecond=0)

        last_sunday_end = last_monday_start + timedelta(days=6, hours=23, minutes=59, seconds=59)

        format_str = "%Y%m%d%H%M%S"
        start = last_monday_start.strftime(format_str)
        end = last_sunday_end.strftime(format_str)

        result = {
            "start": start,
            "end": end
        }
        
        return result
    
    def discord_webhook(self, content):
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.discord_webhook_url, json.dumps(content), headers=headers)
    

    def parser(self, feed_url):
        r = feedparser.parse(feed_url)
        self.r = r.entries

    def parser_arxiv(self, category):
        date = self.get_current_and_last_week()
        client = arxiv.Client()
        search = arxiv.Search(
            query = "cat:%22 {} %22 AND submittedDate:[{} TO {}]".format(' '.join(category), date['start'], date['end']),
            max_results = 10,
            sort_by = arxiv.SortCriterion.SubmittedDate,
            sort_order = arxiv.SortOrder.Descending 
        )
        self.r = list(client.results(search))

    def lists(self):
        NotImplementedError("このメソッドはサブクラスで実装してください。")
    
    def show(self):
        NotImplementedError("このメソッドはサブクラスで実装してください。")