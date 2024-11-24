from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .utils import predict

from .models import User 
from . import models
from .forms import UserForm

from django.db import IntegrityError
from django.http import HttpResponseServerError

import os
# Create your views here.


def register(request):
	forms = UserForm()
	
	if request.method == 'POST':
     
		forms = UserForm(request.POST)
		name = request.POST.get('name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if forms.is_valid():
			try:
				reg = forms.save(commit=False)
				reg.name = name
				reg.username = username
				reg.email = email
				reg.password1 = password1
				reg.password2 = password2
				reg.save()
				messages.success(request, 'You\'ve successfully registered')
				return redirect('prediction:login')
			
			except IntegrityError as e:
				# Handle integrity error (e.g., duplicate email or username)
				messages.error(request, f'Failed to register: {str(e)}')
			
			except Exception as e:
				# Handle other exceptions
				messages.error(request, f'Failed to register: {str(e)}')
		else:
            # Add error messages to the messages framework
			for field, errors in forms.errors.items():
				for error in errors:
					messages.error(request, f'Error in field {field}: {error}')
					
	context = {'forms': forms}
	return render(request, 'prediction/register.html', context)

def account_login(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			models.User.objects.get(username=username)
		except:
			messages.error(request,'User Not Exist!')
		else:
			
			user = authenticate(request,username=username,password=password)

			if (user is not None) and(user.is_active == True):

				login(request,user)
				return redirect('prediction:home')
            
			else:

				messages.error(request,'Username And Password Is Not Valid or User Is No More Active')
	context={}
	return render(request,'prediction/login.html',context)

@login_required
def account_logout(request):

	logout(request)
	return redirect('prediction:login')

 
# @login_required
def home(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        print(images)
        predictions = []
        
        for image in images:
            file_path = default_storage.save('uploads/' + image.name, ContentFile(image.read()))
            absolute_file_path = default_storage.path(file_path)
            print(f"Saved file at {absolute_file_path}")  # Debugging line
            
            if not os.path.exists(absolute_file_path):
                print(f"File {absolute_file_path} does not exist")
                continue
            
            prediction = predict(absolute_file_path)
            predictions.append((file_path, prediction))
        
        print(f"Predictions: {predictions}")
        return render(request, 'prediction/result.html', {'predictions': predictions})

    return render(request,'prediction/home.html',{})

# def results(request):
    
#     return render(request,'prediction/result.html')


