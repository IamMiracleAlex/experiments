from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.views import View
from django.contrib import messages
from users.forms import LoginForm, SignupForm

from users.forms import LoginForm


class LoginView(View):
    '''Login into the application'''
    
    template_name = 'users/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in', extra_tags='success')
                return redirect('index')

            messages.error(request, 'Invalid password or username', extra_tags='danger')
            return render(request, self.template_name, {'form': form})

        messages.error(request, 'Please correct the errors below', extra_tags='danger')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    '''Logout from current session'''

    def get(self, request):
        logout(request)
        messages.success(request, 'Successfully logged out', extra_tags='success')
        return redirect('index')


class SignupView(View):
    '''Sign Up a new user'''

    template_name = 'users/signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
   
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful, please log in', extra_tags='success')
            return redirect('login')

        messages.error(request, 'Please correct the errors below', extra_tags='danger')
        return render(request, self.template_name, {'form': form})


