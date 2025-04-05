from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def about(request):
    return render(request, "about.html")


def post1(request):
    return render(request, "posts/post1.html")


def post2(request):
    return render(request, "posts/post2.html")
