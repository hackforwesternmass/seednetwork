# Seed library views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from seedlibrary.models import Seed
from django.db.models import Q

@login_required
def seed_search(request):
	query = ''
	seed_list = []
	if request.method=='POST':
		query = request.POST['q']
		seed_list = Seed.objects.filter(
			Q(seed_type__startswith=query)|
			Q(crop_type__startswith=query)|
			Q(seed_variety__startswith=query)|
			Q(user__username__startswith=query)
		)

	return render_to_response('seed-search.html',
			{'q':query, 'seed_list':seed_list},
			context_instance=RequestContext(request))