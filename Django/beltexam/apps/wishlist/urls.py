from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^add$', add, name='add'),
    url(r'^add_item$', add_item, name='add_item'),
    url(r'^people$', people, name='people'),
]
