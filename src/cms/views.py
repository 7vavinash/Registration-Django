from django.shortcuts import render, redirect
from .forms import UserCreateForm, LogInForm
from django.contrib import messages
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Restframe work urls
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer



# Create your views here.
@login_required
def home(request):
	return render(request,'home.html',{'title':'Home',})



# Signing up through Inbuilt form
def signup(request):
	form = UserCreateForm(request.POST or None)

	if (form.is_valid()):
		instance = form.save()
		messages.success(request, "You have successfully registered")
		return redirect('/')

	context = {
		'form': form,
		'title': 'Sign Up',
	}
	context.update(csrf(request))

	return render(request, 'signup.html', context)

def login_user(request):
	form = LogInForm(request.POST or None)

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				print (user)

				return redirect("/")

		else:
			messages.error(request, "Incorect Username or Password")

	context = {
		'form': form,
		'title': 'Sign In'
	}

	context.update(csrf(request))
	return render(request, 'signup.html', context)

def logout_user(request):
	logout(request)
	return redirect('/')


class UserDetails(APIView):

	def get(self, request, format=None):
		user = request.user
		serializer = UserSerializer(user)
		return Response(serializer.data)
		