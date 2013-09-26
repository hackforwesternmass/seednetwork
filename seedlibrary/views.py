# Seed library views
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from seedlibrary.forms import SeedForm
from seedlibrary.models import Seed, Event


def home(request):
	return render_to_response('seedlib-home.html',
		{},
		context_instance=RequestContext(request))

def update_seed_events(seed, all_checked_events):
	all_events = Event.objects.filter(show_on_seed_edit=True)
	for e in all_events:
		if e in all_checked_events:
			e.seed.add(seed)
		else:
			e.seed.remove(seed)

@login_required
def seed_create(request):
	seed_form = SeedForm()  
	if request.method == 'POST':
		seed_form = SeedForm(request.POST)
		if seed_form.is_valid():

			seed = Seed.objects.create(
				user = request.user,
				seed_type = seed_form.cleaned_data['seed_type'],
				crop_type = seed_form.cleaned_data['crop_type'],
				seed_variety = seed_form.cleaned_data['seed_variety'],
				seed_description = seed_form.cleaned_data['seed_description'],
				enough_to_share = seed_form.cleaned_data['enough_to_share'],
				year = seed_form.cleaned_data['year'],
				origin = seed_form.cleaned_data['origin']
			)
			seed.save()

			update_seed_events(seed, seed_form.cleaned_data['events'])

			return redirect('seedlibrary.views.seed_create_confirm')
		

	return render_to_response('seed-create.html',
		{"seed_form":seed_form},
		context_instance=RequestContext(request))
	


@login_required
def seed_create_confirm(request):
	return render_to_response('seed-confirm.html',
		{},
		context_instance=RequestContext(request))

        
@login_required
def seeds(request):  
	seed_list = Seed.objects.filter(user=request.user, archived=False)
	seed_archive_list = Seed.objects.filter(user=request.user, archived=True)

	return render_to_response('seeds.html',
		{ "seed_list": seed_list, "seed_archive_list": seed_archive_list },
		context_instance=RequestContext(request))

def fill_seed_from_form(seed, form):
	seed.seed_type = form.cleaned_data['seed_type']
	seed.crop_type = form.cleaned_data['crop_type']
	seed.seed_variety = form.cleaned_data['seed_variety']
	seed.seed_description = form.cleaned_data['seed_description']
	seed.enough_to_share = form.cleaned_data['enough_to_share']
	seed.year = form.cleaned_data['year']
	seed.origin = form.cleaned_data['origin']

@login_required
def seed_edit(request, id):
	seed = get_object_or_404(Seed, pk=id)
	error = None

	if request.method == 'POST':
		form = SeedForm(request.POST)
		if form.is_valid():
			fill_seed_from_form(seed, form)
			seed.save()

			update_seed_events(seed, form.cleaned_data['events'])

			return redirect('seedlibrary.views.seeds')
	else:
		data = {}
		data['seed_type'] = seed.seed_type
		data['crop_type'] = seed.crop_type
		data['seed_variety'] = seed.seed_variety
		data['seed_description'] = seed.seed_description
		data['enough_to_share'] = seed.enough_to_share
		data['year'] = seed.year
		data['origin'] = seed.origin
		e_ids = []
		for e in seed.event_set.all():
			e_ids.append(e.id)
		data['events'] = e_ids

		form = SeedForm(data)

	return render_to_response('seed-edit.html',
		{ "seed":seed, "form": form, "error": error },
        context_instance=RequestContext(request))

@login_required
def seed_confirm_archive(request, id):
	seed = get_object_or_404(Seed, pk=id, user=request.user)
	error = None

	if request.method == 'POST':
		if request.POST['command'] == 'archive' and not seed.archived:
			seed.archived = True
			seed.save()
		elif request.POST['command'] == 'unarchive' and seed.archived:
			seed.archived = False
			seed.save()

		return redirect('seedlibrary.views.seeds')

	return render_to_response('seed-confirm-archive.html',
			{ "seed":seed, "error": error },
			context_instance=RequestContext(request))

@login_required
def events(request):
	event_list = Event.objects.all()

	return render_to_response('events.html',
			{ "event_list": event_list,},
            context_instance=RequestContext(request))

@login_required
def seeds_at_event(request, id):
	event = get_object_or_404(Event, pk=id)

	seed_list = event.seed.all()

	return render_to_response('seeds-at-event.html',
			{ "seed_list": seed_list, "event": event },
			                  context_instance=RequestContext(request))
