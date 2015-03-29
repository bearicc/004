from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^blog/admin/', include(admin.site.urls)),
    url(r'^login/$', 'mysite.views.login', name='login'),
    url(r'^your-name/', 'mysite.views.get_name'),
    url(r'^thanks/(?P<name>\w+)/$', 'mysite.views.thanks')
)
