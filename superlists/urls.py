from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'superlists.views.home', name='home'),
    url(r'^$', 'lists.views.home_page', name='home'),

    # not using this just yet...
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
