from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from resume.forms import ContactForm


def index(request):
    return render(request, 'resume/index.html')


def about(request):
    return render(request, 'resume/about.html')


def contact_me(request):
    form = ContactForm()
    context = {'form_success': False}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['form_success'] = True
    context['form'] = form
    return render(request, 'resume/contact_me.html', context)
