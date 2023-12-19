from django.db import models
from users.models import User
import uuid
class PostModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    edited_on = models.DateTimeField(auto_now_add=True)

class CommentModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    post = models.ForeignKey(PostModel, related_name="post", on_delete=models.CASCADE)
    body = models.TextField()
    comment_on = models.DateTimeField(auto_now=True)
    edited_on = models.DateTimeField(auto_now_add=True)