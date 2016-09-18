from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lead/create$', views.lead_create, name='create'),
]
