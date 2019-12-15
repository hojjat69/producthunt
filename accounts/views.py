from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signin(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if (user is not None):
          auth.login(request,user)
          return redirect('home')
        else:
          return render (request, 'accounts/signin.html', {'error':'username or password is not correct'})
    else:
        return render (request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        # user want to do sign-up
        if request.POST['password']==request.POST['password2']:
            try:
                user_new = User.objects.get(username=request.POST['username'])
                return render (request, 'accounts/signup.html', {'error':'Username is Already Taken'})
            except User.DoesNotExist:
                user_new = User.objects.create_user(request.POST['username'],password=request.POST['password'],email=request.POST['email'])
                auth.login(request,user_new)
                return redirect('home')
        else:
            return render (request, 'accounts/signup.html', {'error':'Passwords dont match'})

    else:
        # user just enter to sign-up page
        return render (request, 'accounts/signup.html')


def signout(request):
    # Need to rout to homepage
    # and dont forgte to logout
    auth.logout(request)
    return redirect('home')
    

