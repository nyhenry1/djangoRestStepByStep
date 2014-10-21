from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = patterns(
	'',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^snippets/$', views.SnippetList.as_view()), 
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#    url(r'^', include('snippets.urls')),
)
urlpatterns = format_suffix_patterns(urlpatterns)
