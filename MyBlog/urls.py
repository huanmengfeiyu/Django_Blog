from django.conf.urls import url
from . import views

# app_name='Blog'
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^list$', views.querytion_list, name='list')
]
