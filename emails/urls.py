from django.conf.urls import patterns, include, url

urlpatterns = patterns('emails.views',
    url(r'^templates/$', 'email_templates', name='email_templates'),
    url(r'^templates/create$', 'create_email_template', name='create_email_template'),
    url(r'^templates/(?P<pk>\d+)$', 'view_email_template', name='view_email_template'),
    url(r'^templates/(?P<pk>\d+)/edit$', 'edit_email_template', name='edit_email_template'),
    url(r'^templates/(?P<pk>\d+)/delete$', 'delete_email_template', name='delete_email_template'),

    url(r'^accounts/$', 'accounts', name='accounts'),
    url(r'^accounts/create$', 'create_account', name='create_account'),
    url(r'^accounts/(?P<pk>\d+)$', 'view_account', name='view_account'),
    url(r'^accounts/(?P<pk>\d+)/edit$', 'edit_account', name='edit_account'),
    url(r'^accounts/(?P<pk>\d+)/delete$', 'delete_account', name='delete_account'),

    url(r'^send$', 'send_email', name='send_email'),
)
