from django.conf.urls import patterns, include, url

urlpatterns = patterns('wizard.views',
    url(r'^$', 'index', name='wizard'),
    url(r'^site$', 'site', name='wizard_site'),
    url(r'^social$', 'social', name='wizard_social'),
    url(r'^admin$', 'admin', name='wizard_admin'),
)
