from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add$', add_playlist, name='add'),
    url(r'^add_song/(?P<playlist_id>\d+)$', add_song, name='addsong')
]
