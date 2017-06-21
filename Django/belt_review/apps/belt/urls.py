from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^/book_home$', book_home, name='book_home'),
    url(r'^/add_book$', add_book, name='add_book'),
    url(r'^/logout$', logout, name='logout'),
]
