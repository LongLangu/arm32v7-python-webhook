import os
from abc import ABCMeta


class Config(metaclass=ABCMeta):
    
    def __init__(self, env):
        self.env = env

    def get_webhook_url(self, ):
        NotImplementedError("このメソッドはサブクラスで実装してください。")
    

class Development(Config):
    
    def __init__(self, ):
        super().__init__('development')
    
    def get_webhook_url(self):
        return 

        

class Test(Config):

    def __init__(self, ):
        super().__init__('test')
    
    def get_webhook_url(self):
        return 'mock'

class Production(Config):

    def __init__(self, ):
        super().__init__('production')
        self.webhook_url = os.environ['WEBHOOK_URL']

    def get_webhook_url(self):
        return self.webhook_url
