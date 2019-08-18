from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def registration(request):
	if request.method == 'POST':
		print("request method is POST")
		if request.POST['username']=='' or request.POST['email']=='' or request.POST['password1']=='' or request.POST['first_name']=='':
			messages.info(request,"please fill details correctly")
			return redirect('registration')
        
		first_name=request.POST['first_name']
		last_name =request.POST['last_name']
		username  =request.POST['username']
		email     =request.POST['email']
		password1 =request.POST['password1']
		password2 =request.POST['password2']
		if password1==password2 :
			if User.objects.filter(username=username).exists():
				
				messages.info(request,"username_already_exist")
				print("username_already_exist")
				return redirect('registration')

			
			elif User.objects.filter(email=email).exists():
				
				messages.info(request,'Already_registered_email')
				print("Already_registered_email")
				return redirect('registration')

			else:
				user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				user.save()
				user=auth.authenticate(username=username,password=password1)
				print("save everything")
				auth.login(request,user)
				return redirect('/sahuweb')

				
			
		else:
			messages.info(request,'password not match')
			print("password not matched")
			return redirect('registration')
		return redirect('/sahuweb')
		
	else:
		print("request is not POST method")
		return render(request,"register.html")



def login(request):
	print(request.method)
	if request.method=='POST':
		print(request.method)
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			print("login attempt")
			return redirect('/sahuweb')

		else:
			messages.info(request,'invailid username/password')
			print("invailid username/password")
			return redirect('login')
	else:
		print("get_method has been uses")
		return render(request,"login.html")


def logout(request):
	print(request.method)
	auth.logout(request)
	return redirect('/sahuweb')
	# return redirect('/account/login')
			
