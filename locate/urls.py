'''
    File name: locate/urls.py
    Author: Uday Singh
    Python Version: 2.7
'''

from django.conf.urls import url
from .apis import LocationsViewSet, PlacesViewSet
from .views import plot_map, locations_list, add_location


urlpatterns = [
    url(r'^$', LocationsViewSet.as_view(), name='Locations'),
    url(r'^map/$', plot_map, name='Plot Map'),
    url(r'^places/$', PlacesViewSet.as_view(), name='Places'),
    url(r'^locations/$', locations_list, name='locations'),
    url(r'^add_location/$', add_location, name='add_location'),
]