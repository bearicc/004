from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})

def login(request):
    current_name = ' '
    return render(request, 'login.html')#, {'current_name', current_name})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/'+form.cleaned_data['your_name']+'/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def thanks(request, name):
    return HttpResponse('How are you, '+name+'!')
