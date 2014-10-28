from django.conf.urls import patterns, include, url

urlpatterns = patterns('settings.views',
    url(r'^$', 'index', name='settings')
)
