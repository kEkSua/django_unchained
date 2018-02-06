from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from resume.forms import ContactForm
from django.contrib.auth.views import login


def index(request):
    return render(request, 'resume/index.html')


@login_required
def inner_page(request):
    return render(request, 'resume/inner_page.html')


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


def my_login(request, *args, **kwargs):
    if request.method == 'POST' and not request.POST.get('remember', None):
        request.session.set_expiry(0)
    return login(request, *args, **kwargs)
