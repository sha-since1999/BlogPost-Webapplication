from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import cards

def index(request):
	cards_list=cards.objects.all()
	return render(request,"index.html",{"cards_list":cards_list})
def register(request):
	return redirect('/account/register')
def login(request):
	return redirect('/account/login')