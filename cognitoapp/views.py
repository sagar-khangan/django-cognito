from django.shortcuts import render, HttpResponse, render_to_response
from warrant.exceptions import *
from forms import *
from utils import *
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

class ActivateView(View):

    @csrf_exempt
    def get(self, request):
        form = ActivateForm()
        return render(request, ("cognitoapp/activate_form.html"), {'form': form})

    @csrf_exempt
    def post(self, request):
        form = ActivateForm()
        u = get_cognito_obj(request.POST['username'])
        try:
            u.new_password_challenge(request.POST[' activation_code'], request.POST['password'])
            return render(request, ("cognitoapp/login.html"), {'form': form})
        except Exception as e:
            err = "Not activated.. Please try again to activate"
            return render(request, ("cognitoapp/activate_form.html"), {'form': form, 'error': err})

class LoginView(View):

    access_token, username = None, None
    @csrf_exempt
    def get(self, request):
        form = LoginForm
        if self.access_token is not None:
            u = get_cognito_obj(username=self.username, access_token=self.access_token)
            try:
                u.logout()
            except Exception as e:
                print e
        return render(request, ("cognitoapp/login.html"), {'form': form})

    @csrf_exempt
    def post(self, request):
        form = LoginForm
        u = get_cognito_obj(request.POST['username'])
        self.access_token = u.access_token
        try:
            u.authenticate(request.POST['password'])
            return render(request, ("cognitoapp/success.html"))
        except Exception as e:
            err = "Invalid credentials...Please try again"
            return render(request, ("cognitoapp/login.html"), {'form': form, 'error': err})
