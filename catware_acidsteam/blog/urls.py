from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home'),
	url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'read'),
	url(r'^contact/$', 'contact'),
	url(r'^articlef/$', 'article'),
	url(r'^addition/(?P<number1>\d+)/(?P<number2>\d+)/$', 'addition'),
	url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'),
)	
