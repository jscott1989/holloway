from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'holloway.views.index', name='index'),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^emails/', include('emails.urls')),
    url(r'^wizard/', include('wizard.urls')),

    (r'^accounts/', include('allauth.urls')),
)
