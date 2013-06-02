# Seed library views
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

def seed_search(request):
	return redirect('seednetwork.views.home')