from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^acceuil/$', 'home'),
	url(r'^$', 'tpl'),
	url(r'^addition/(?P<number1>\d+)/(?P<number2>\d+)/$', 'addition'),
	url(r'^article/(?P<id_article>\d+)/$', 'view_article'),
	url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'),
)	
