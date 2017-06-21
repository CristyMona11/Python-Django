from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^generated$', generate),
    url(r'^reset$', reset)
]
