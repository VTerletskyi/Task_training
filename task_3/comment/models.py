from django.db import models
from post.models import Post
from user.models import User


class Comment(models.Model):

    comment_author = models.ForeignKey(User, default=False, verbose_name="Автор коментаря", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Стаття", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Коментар")

    def __str__(self):
        return "{} коментує: {}".format(self.comment_author.user_name, self.post.title)