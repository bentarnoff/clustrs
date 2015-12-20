import autocomplete_light

autocomplete_light.autodiscover()

from django.conf.urls import include, url
import dashboard.views

urlpatterns = [

	#user auth
    url(r'^login$', 'dashboard.views.login'),
    url(r'^auth$', 'dashboard.views.auth_view'),
    url(r'^logout$', 'dashboard.views.logout'),
    url(r'^invalid$', 'dashboard.views.invalid_login'),

    #dashboard
    url(r'^hello$', 'dashboard.views.hello'),
    url(r'^my_clustrs$', 'dashboard.views.my_clustrs'),
    url(r'^remove$', 'dashboard.views.remove'),
    url(r'^add$', 'dashboard.views.add'),
    url(r'^my_queue$', 'dashboard.views.my_queue'),
    url(r'^qremove$', 'dashboard.views.qremove'),
    url(r'^qadd$', 'dashboard.views.qadd'),

    #registration
    url(r'^', include('registration.backends.default.urls')),

    #autocomplete
    url(r'^autocomplete/', include('autocomplete_light.urls')),
]