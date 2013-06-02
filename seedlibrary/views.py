# Seed library views
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from seedlibrary.forms import SeedForm
from seedlibrary.models import Seed


def home(request):
	return render_to_response('home.html',
		{},
		context_instance=RequestContext(request))

@login_required
def seed_create(request):
	seed_form = SeedForm()  
	if request.method == 'POST':
		seedform = SeedForm(request.POST)
		if seedform.is_valid():
			seed = Seed.objects.create(
                                user = request.user,
				seed_type = seedform.cleaned_data['seed_type'],
				crop_type = seedform.cleaned_data['crop_type'],
				seed_variety = seedform.cleaned_data['seed_variety'],
                                seed_description = seedform.cleaned_data['seed_description'],
				enough_to_share = seedform.cleaned_data['enough_to_share'],
                                year = seedform.cleaned_data['year'],
                                origin = seedform.cleaned_data['origin']
				)
			seed.save()
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
	seeds_list = Seed.objects.filter(user=request.user)

	return render_to_response('seeds.html',
		{ "seed_list": seeds_list },
		context_instance=RequestContext(request))

def fill_seed_from_form(seed, form):
        seed_type = form.cleaned_data['seed_type'],
        crop_type = form.cleaned_data['crop_type'],
        seed_variety = form.cleaned_data['seed_variety'],
        seed_description = form.cleaned_data['seed_description'],
        enough_to_share = form.cleaned_data['enough_to_share'],
        year = form.cleaned_data['year'],
        origin = form.cleaned_data['origin']



@login_required
def edit_seed(request):
	seed = request.seed
	s = get_seed(seed)
	error = None

	if request.method == 'POST':
		form = SeedForm(request.POST)
		if form.is_valid():
			fill_seed_from_form(s, form)
			s.save()
			return redirect('seedlibrary.views.seeds')
	else:
		data = {}
		data['seed_type'] = seed.seed_type
		data['crop_type'] = seed.crop_type
		data['seed_variety'] = seed.seed_variety
		data['seed_description'] = seed.description
		data['enough_to_share'] = seed.enough_to_share
		data['year'] = seed.year
		data['origin'] = seed.origin

		form = SeedForm(data)

	return render_to_response('seed-edit.html',
		{ "form": form, "error": error },
        context_instance=RequestContext(request))


	
	
