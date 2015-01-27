from django.conf.urls import patterns, include, url
from django.contrib import admin

from snippets import views

urlpatterns = patterns('',

    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    url(r'^admin/', include(admin.site.urls)),
)
