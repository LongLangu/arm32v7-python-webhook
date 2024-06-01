import argparse

from webhook.tech_webhook import ArxivWebhook, QiitaTrendWebhook, TechTrendWebhook, ZennTrendWebhook

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='選択された引数にてそのトレンドを取得します。'
    )

    parser.add_argument(
        '-si', 
        '--site', 
        help='どのサイトのトレンドを取得するか選択します。', 
        choices=['zenn', 'zenn-topic', 'qiita', 'qiita-topic', 'tech', 'arxiv'],
        required=True
    )

    args = parser.parse_args()
    site = args.site

    if(site == 'zenn'):
        zenn = ZennTrendWebhook()
        zenn.lists()
    elif(site == 'qiita'):
        qiita = QiitaTrendWebhook()
        qiita.lists()
    elif(site == 'tech'):
        tech = TechTrendWebhook()
        tech.lists()
    elif(site == 'arxiv'):
        arxiv = ArxivWebhook(['cs.CV', 'cs.AI'])
        arxiv.lists()