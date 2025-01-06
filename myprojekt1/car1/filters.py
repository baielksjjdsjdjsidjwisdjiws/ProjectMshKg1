from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt', 'lt'],
            'year': ['gt', 'lt'],
            'CarMake_name': ['exact'],
            'volum': ['exact']
        }