from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = patterns(
	'snippets.views',
	
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'api_root'),
    url(r'^snippets/$', views.SnippetList.as_view(),
			name = 'snippet-list'), 
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),
			name = 'snippet-detail'),
#    url(r'^', include('snippets.urls')),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),
						name = 'snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(),
			name = 'user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
			name = 'user-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
)
urlpatterns = format_suffix_patterns(urlpatterns)
