from django.db import models
from user.models import User


class Post(models.Model):

    user = models.ForeignKey(User, verbose_name="Користувач", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок", max_length=256)
    body_post = models.TextField(verbose_name="Стаття")
    image = models.ImageField(upload_to='post_image/')

    def __str__(self):
        return "Заголовок: {}".format(self.title)

