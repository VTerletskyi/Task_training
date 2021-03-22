from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, ListView


class PostDetailView(DetailView):
    model = Post
    template_name = "post/details_view.html"
    context_object_name = "post"


class PostView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "post"


# def index(request):
#     news = Post.objects.all()
#     #   ---prefetch_related("postimage_set")
#     return render(request, "post/index.html", {"news": news})


def newpost(request):
    error = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Потрібно правильно заповнити форму"
    form = PostForm()

    date = {
        "form": form,
        "error": error
    }
    return render(request, "post/newpost.html", date)

