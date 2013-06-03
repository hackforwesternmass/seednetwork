from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from seednetwork import settings
from seednetwork.forms import SeedNetworkAuthForm, SeedNetworkPasswordChangeForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seednetwork.views.home', name='home'),
    url(r'^seedlibrary/', include('seedlibrary.urls')),

    url(r'^$', 'seednetwork.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user management
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html', 'authentication_form':SeedNetworkAuthForm}),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name':'logout.html', 'next_page':'/'}),
	(r'^accounts/profile/$', 'seednetwork.views_user.profile'),
	(r'^accounts/member/(?P<mid>[0-9]+)$', 'seednetwork.views_user.member'),
	(r'^accounts/profile-edit/$', 'seednetwork.views_user.edit_profile'),

    (r'^accounts/new-user/$', 'seednetwork.views_user.new_user'),


	(r'^accounts/reset-password/$', 'django.contrib.auth.views.password_reset',
		 {'template_name':'password_reset.html',
		  'email_template_name':'password_reset_email.html'}),

	(r'^accounts/reset-password/done/$', 'django.contrib.auth.views.password_reset_done',
		 {'template_name':'password_reset_done.html'}),

	(r'^accounts/reset-password-confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
	 'django.contrib.auth.views.password_reset_confirm', {'template_name':'password_reset_confirm.html'}),

	(r'^accounts/reset-password-complete/$', 'django.contrib.auth.views.password_reset_complete',
		{'template_name':'password_reset_complete.html'}),




	(r'^accounts/change-password/$', 'django.contrib.auth.views.password_change',
		 {'template_name':'password_change.html', 'password_change_form':SeedNetworkPasswordChangeForm}),

	(r'^accounts/change-password/done/$', 'django.contrib.auth.views.password_change_done',
		 {'template_name':'password_change_done.html'}),
)

if not settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	                        )