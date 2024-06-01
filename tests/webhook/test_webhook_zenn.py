import os
import sys
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.append('{}'.format(os.getcwd()))

from tests.mocked import mocked_feedparser_parse, mocked_requests_post
from webhook.tech_webhook import ZennTrendWebhook


class TestZennTrendWebhook:

    # 記事を取得できる
    def test_get_trand_articles(self, mocker):

        mocker.patch("feedparser.parse", side_effect=mocked_feedparser_parse)
        mocker.patch("requests.post", side_effect=mocked_requests_post)

        webhook = ZennTrendWebhook()
        with patch.dict("os.environ", {"ENVIRONMENT": "test"}):
            request = webhook.lists()

        assert request.status_code, 201
        assert request.status_code, 'OK' 