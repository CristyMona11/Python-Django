from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^submit$', submit, name='submit'),
    url(r'^remove_course/(?P<id>\d+)/$', remove, name='remove'),
    url(r'^deleted/(?P<id>\d+)/$', deleted, name='deleted'),
    url(r'^keep_course$', keep, name='keep')
]
