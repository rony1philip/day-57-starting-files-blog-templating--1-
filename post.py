import requests


class Post:
    def __init__(self):
        self.all_posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
        self.ids = []
        for post in self.all_posts:
            self.ids.append(str(post['id']))