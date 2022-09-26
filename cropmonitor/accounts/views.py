from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from accounts.models import FarmerProfile


from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



from django.contrib import messages

from django.utils.decorators import method_decorator

from .forms import ProfileForm, form_validation_error
from farm.models import Profile
from django.views import View

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('myfarms')
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')



 
def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.is_active = True
                user.first_name = first_name
                user.last_name = last_name
                user.save()
               # auth.login(request,user)
                return redirect('login')
        else:
            return render (request,'accounts/register.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/register.html')
  

@login_required(login_url='login')
def home(request):
  template = loader.get_template('dashboard/home.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))



@login_required(login_url='login')
def myprofile(request):
  template = loader.get_template('accounts/myprofile.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'accounts/myprofile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('myprofile')







def contactus(request):
  template = loader.get_template('dashboard/contactus.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def faq(request):
  template = loader.get_template('dashboard/faq.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))



