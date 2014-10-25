from django.conf.urls import patterns, include, url

urlpatterns = patterns('contacts.views',
    url(r'^$', 'index', name='contacts'),
    url(r'^create$', 'create_contact', name='create_contact'),
    url(r'^(?P<pk>\d+)$', 'view_contact', name='view_contact'),
    url(r'^(?P<pk>\d+)/edit$', 'edit_contact', name='edit_contact'),
    url(r'^(?P<pk>\d+)/delete$', 'delete_contact', name='delete_contact'),
    url(r'^groups$', 'groups', name='groups'),
)
