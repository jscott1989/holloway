from django.conf.urls import patterns, include, url

urlpatterns = patterns('contacts.views',
    url(r'^$', 'index', name='contacts'),
    url(r'^groups$', 'groups', name='groups'),
)
