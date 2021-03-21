from django.db import models


class User(models.Model):

    user_name = models.CharField(verbose_name="Ім'я користувача", max_length=256)
    email = models.EmailField(blank=True, null=True, max_length=200, verbose_name="email")
    password = models.CharField(verbose_name="Пароль", max_length=10)

    def __str__(self):                                                                                                                          
        return "Користувач: {}".format(self.user_name)
