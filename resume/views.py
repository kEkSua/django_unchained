from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'resume/index.html')


@login_required
def about(request):
    return render(request, 'resume/about.html')
