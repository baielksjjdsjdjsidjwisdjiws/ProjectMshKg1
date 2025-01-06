from .views import CarMakeViewSet, CarModelViewSet, CarViewSet
from django.urls import path


urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car'),

    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                          'delete': 'destroy'}), name='car_detail')
]