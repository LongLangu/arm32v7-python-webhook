def mocked_feedparser_parse(*args, **kwargs):
    class MockResponse:
        def __init__(self):
            self.entries = [
                {
                    "title": "テスト1用のタイトル",
                    "title_detail": {},
                    "summary": "ここに記事の要約が入る。",
                    "summary_detail": {},
                    "links": [],
                    "link": "mock",
                    "id": "mock",
                    "guidislink": False,
                    "published": "Mon, 31 May 2021 13:46:25 GMT",
                    "authors": [
                        {
                        "name": "tester"
                        }
                    ],
                    "published_parsed": [ 2021, 5, 31, 13, 46, 25, 0, 151, 0 ],
                    "author": "tester",
                    "author_detail": {
                        "name": "tester"
                    }
                }
            ]

    return MockResponse()

def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.__text = text
            self.__status_code = status_code

        @property
        def text(self):
            return self.__text
        
        @property
        def status_code(self):
            return self.__status_code

        def raise_for_status(self):
            if self.__status_code != 200:
                raise Exception("requests error")
    
    if args[0] == 'mock':
        return MockResponse("OK", 201)
    
    return MockResponse(None, 404)