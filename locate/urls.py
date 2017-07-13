'''
    File name: locate/urls.py
    Author: Uday Singh
    Python Version: 2.7
'''

from django.conf.urls import url
from .apis import LocationsViewSet, PlacesViewSet


urlpatterns = [
    url(r'^$', LocationsViewSet.as_view()),
    url(r'^places/$', PlacesViewSet.as_view()),
]