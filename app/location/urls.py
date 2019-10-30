from django.urls import path

from . import views

urlpatterns = [
    path('', views.LocationList.as_view(), name='index'),
    path('<int:location_key>', views.LocationDetail.as_view(), name='location_detail'),
    path('filter', views.LocationFilter.as_view(), name='location_filter')
]
