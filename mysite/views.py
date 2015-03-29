from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse

class SignupForm(forms.Form):
    name   = forms.CharField(label='Name', max_length=32)
    passwd1 = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    passwd2 = forms.CharField(label='Confirm', max_length=32, widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        if self.data['passwd1'] and  self.data['passwd1'] != self.data['passwd2']:
            raise forms.ValidationError('Passwords are not the same')
        return super(SignupForm, self).clean(*args, **kwargs)

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})

def login(request):
    current_name = ' '
    return render(request, 'login.html')#, {'current_name', current_name})

def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/'+form.cleaned_data['name']+'/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def thanks(request, name):
    return HttpResponse('Thanks for registration, '+name+'!')
