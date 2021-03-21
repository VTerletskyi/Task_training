from django.shortcuts import render
from .models import Post


def index(request):
    news = Post.objects.all()
    #   ---prefetch_related("postimage_set")
    return render(request, "post/index.html", {"news": news})
