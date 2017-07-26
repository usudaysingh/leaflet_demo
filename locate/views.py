'''
    File name: locate/views.py
    Author: Uday Singh
    Python Version: 2.7
'''

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import locate

@login_required
def plot_map(request):
	if request.method == 'GET':
		template = 'map.html'
		return render(request, template,{'user':request.user})

@login_required
def locations_list(request):
	template = 'locations.html'
	if request.method == 'GET':
		points = locate.objects.all()
		return render(request, template,{'user':request.user, 'points':points})
	else:
		search = request.POST.get('search')
		points = locate.objects.filter(name__icontains=search)
		return render(request, template, {'points':points,'search_value':search})

@login_required
def add_location(request):
	template = 'create_new_location.html'
	if request.method == 'GET':
		return render(request, template)
	else:
		pdata = {
			'google_map_name': request.POST.get('google_map_name'),
			'name':request.POST.get('name'),
			'latitude':request.POST.get('latitude'),
			'longitude':request.POST.get('longitude')
		}

		try:
			locate.objects.create(**pdata)
		except Exception as e:
			error = str(e)
			return render(request, template, {'error':error})

		return render(request, template, {'success':'Location Added Successfully.'})