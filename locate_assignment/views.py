'''
    File name: locate_assignment/views.py
    Author: Uday Singh
    Python Version: 2.7
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from locate.models import AppUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
	error = ''
	template = 'login.html'
	if request.method == 'GET':
		if request.user.is_authenticated():
		    return HttpResponseRedirect('/locate/map/')
		else:
			return render(request, template, {'error':error})
	else:
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect('/locate/map')
		except Exception as e:
		    error = str(e)
		    return render(request, template, {'error':error})
	        
def logout_user(request):
	if request.method == 'GET':
		logout(request)
		return HttpResponseRedirect('/login/')