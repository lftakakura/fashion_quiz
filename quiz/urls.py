from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new-lead$', views.save_lead, name='save_lead'),
    url(r'^(?P<token>[0-9a-z-]+)$', views.index, name='index')
]
