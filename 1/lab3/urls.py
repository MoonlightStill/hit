from django.conf.urls import patterns, include, url
from django.contrib import admin  


admin.autodiscover()
urlpatterns = patterns('',

    url(r'^addbook/$','Library.views.addbook'),
    url(r'^savebook/$','Library.views.savebook'),
    url(r'^addauthor/$','Library.views.addauthor'),
    url(r'^saveauthor/$','Library.views.saveauthor'),
    url(r'^$','Library.views.index'),
    url(r'^search/$','Library.views.search'),
    url(r'^showauthor/$','Library.views.showauthor'),
    url(r'^showbook/(\d+)/$','Library.views.showbook',name="showbook"),
    url(r'^delete/(\d+)/$','Library.views.delete',name="delete"),
    url(r'^refresh/(\d+)/$','Library.views.refresh',name="refresh"),
    url(r'^change/$','Library.views.change'),
    url(r'^change/$','Library.views.change'),
    url(r'^saveall/$','Library.views.saveall'),
    url(r'^test/$', 'Library.views.test'),


)
