from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^$', 'seedlibrary.views.home', name='home'),
)
