from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
#jadmin.autodiscover()

urlpatterns = patterns(
	'snippets.views',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
#    url(r'^', include('snippets.urls')),
)
urlpatterns = format_suffix_patterns(urlpatterns)
