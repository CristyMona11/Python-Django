from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^add_artist$', add_artist, name='add_artist'),
    url(r'^added_artist$', added_artist, name='added_artist'),
    url(r'^added_song/(?P<album_id>\d+)$', added_song, name='added_song'),
]
