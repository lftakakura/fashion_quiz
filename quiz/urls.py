from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<token>[0-9a-z-]+)/$', views.quiz_start, name='start'),
    url(r'^save$', views.quiz_save, name='save'),
    url(r'^(?P<token>[0-9a-z-]+)/done/$', views.quiz_done, name='done')
]
