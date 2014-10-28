from django.conf.urls import patterns, include, url

urlpatterns = patterns('emails.views',
    url(r'^templates/$', 'email_templates', name='email_templates'),
    url(r'^templates/create$', 'create_email_template', name='create_email_template'),
    url(r'^templates/(?P<pk>\d+)$', 'view_email_template', name='view_email_template'),
    url(r'^templates/(?P<pk>\d+)/edit$', 'edit_email_template', name='edit_email_template'),
    url(r'^templates/(?P<pk>\d+)/delete$', 'delete_email_template', name='delete_email_template'),
    url(r'^send$', 'send_email', name='send_email'),
)
