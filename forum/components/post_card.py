from django_unicorn.components import UnicornView
from forum.models import PostModel

class PostCardView(UnicornView):
    post: PostModel = None
    def mount(self):
        self.post = self.component_kwargs.get('post_content')