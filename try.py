import requests

class haha():
    def __init__(self, url):
        self.url = url
    
    def __enter__(self):
        response = requests.get(self.url)
        html = response.content.decode('utf-8')
        return html

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

url = 'https://www.baidu.com'
with haha(url) as t:
    print(t)