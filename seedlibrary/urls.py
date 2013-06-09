from django.conf.urls import patterns, include, url

from seedlibrary import views, views_search

urlpatterns = patterns('',
   url(r'^$', 'seedlibrary.views.home', name='home'),
   url(r'^seeds/create/$', 'seedlibrary.views.seed_create'),
   url(r'^seeds/create-confirm/$', 'seedlibrary.views.seed_create_confirm'),
   url(r'^seeds/$', 'seedlibrary.views.seeds'),
   url(r'^seeds/edit/(?P<id>[0-9]+)$', 'seedlibrary.views.seed_edit'),
   url(r'^seeds/confirm-archive/(?P<id>[0-9]+)$', 'seedlibrary.views.seed_confirm_archive'),
   url(r'^search/$', 'seedlibrary.views_search.seed_search'),
 
)


