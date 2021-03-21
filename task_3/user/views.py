from django.shortcuts import render, redirect
from .forms import UserForm


def registration(request):
    error = ""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Потрібно правильно заповнити форму"
    form = UserForm()

    date = {
        "form": form,
        "error": error
    }
    return render(request, "user/index.html", date)