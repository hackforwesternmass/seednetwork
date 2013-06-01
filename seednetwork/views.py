from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from seednetwork.forms import MemberInfoForm

from seednetwork.models import MemberInfo

def home(request):

	login_form = AuthenticationForm()
	create_user_form = UserCreationForm()
	member_info_form = MemberInfoForm()

	return render_to_response('home.html',
			{ 'login_form': login_form,
			  'create_user_form': create_user_form,
			  'member_info_form': member_info_form
			},
			context_instance=RequestContext(request))