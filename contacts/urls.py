from django.conf.urls import patterns, include, url

urlpatterns = patterns('contacts.views',
    url(r'^$', 'index', name='contacts'),
    url(r'^create$', 'create_contact', name='create_contact'),
    url(r'^import$', 'import_contacts', name='import_contacts'),
    url(r'^import_confirm$', 'import_contacts_confirm', name='import_contacts_confirm'),
    url(r'^(?P<pk>\d+)$', 'view_contact', name='view_contact'),
    url(r'^(?P<pk>\d+)/edit$', 'edit_contact', name='edit_contact'),
    url(r'^(?P<pk>\d+)/delete$', 'delete_contact', name='delete_contact'),
    url(r'^groups$', 'groups', name='groups'),
    url(r'^groups/create$', 'create_group', name='create_group'),
    url(r'^groups/(?P<pk>\d+)$', 'view_group', name='view_group'),
    url(r'^groups/(?P<pk>\d+)/edit$', 'edit_group', name='edit_group'),
    url(r'^groups/(?P<pk>\d+)/delete$', 'delete_group', name='delete_group'),
)
