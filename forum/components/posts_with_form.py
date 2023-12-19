from django_unicorn.components import UnicornView
from forum.models import PostModel

class PostsWithFormView(UnicornView):
    posts: PostModel = None
    body:str = ""

    def mount(self):
        self.update()

    def update(self):
        self.posts = PostModel.objects.all().order_by('-posted_on')[:3]
        self.body = ""

    def save(self):
        PostModel.objects.create(
            user = self.request.user,
            body = self.body
        )
        self.update()

    def see_more(self):
        self.posts = PostModel.objects.all().order_by('-posted_on')
