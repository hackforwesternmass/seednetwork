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
		seed_list = Seed.objects.all()
		for word in query.split():
			word = word.lower()
			seed_list = seed_list.filter(
				Q(seed_type__icontains=word)|
				Q(crop_type__icontains=word)|
				Q(seed_variety__icontains=word)|
				Q(user__memberinfo__town__icontains=word)|
				Q(user__username__icontains=word)
			)

	return render_to_response('seed-search.html',
			{'q':query, 'seed_list':seed_list},
			context_instance=RequestContext(request))