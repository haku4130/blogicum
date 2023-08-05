from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    return render(request, template)


def post_detail(request):
    template = 'blog/detail.html'
    return render(request, template)
