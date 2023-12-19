from django_unicorn.components import UnicornView
from forum.models import CommentModel, PostModel

class PostWithCommentsView(UnicornView):
    post: PostModel = None
    comments: CommentModel = None
    body:str = ""
    pk = None
    no_of_comment:int = 0

    def mount(self):
        self.pk = self.request.path_info.strip('/').split('/')[-1]
        self.update()

    def save_comment(self):
        CommentModel.objects.create(
            post = self.post,
            user = self.request.user,
            body = self.body
        )
        self.update()

    def update(self):
        self.post = PostModel.objects.get(id = self.pk)
        self.no_of_comment = self.post.post.count()
        self.comments = self.post.post.all().order_by('-comment_on')[:3]

    def see_more(self):
        self.comments = self.post.post.all().order_by('-comment_on')
