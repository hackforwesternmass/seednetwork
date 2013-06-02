from django.conf.urls import patterns, include, url

from seedlibrary import views

urlpatterns = patterns('',
   url(r'^$', 'seedlibrary.views.home', name='home'),
   url(r'^seeds/create/$', 'seedlibrary.views.seed_create'),
   url(r'^seeds/confirm/$', 'seedlibrary.views.seed_create_confirm'),
   url(r'^seeds/$', 'seedlibrary.views.seeds'),
   url(r'^seeds/edit/$', 'seedlibrary.views.edit_seed'),
 
)


