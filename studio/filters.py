import django_filters

from .models import *

class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = {'status':['exact'],'completed':['exact'],'declined':['exact']}
