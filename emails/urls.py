from django.conf.urls import patterns, include, url

urlpatterns = patterns('emails.views',
    url(r'^$', 'index', name='emails'),
)
