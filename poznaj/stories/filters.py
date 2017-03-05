from django.contrib.gis.geos import GEOSGeometry
from rest_framework import filters
from rest_framework.exceptions import ValidationError

WRONG_LAT_LONG_TEXT = 'Provide float for latitude and longitude'


class FirstPointFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        lat = request.query_params.get('lat', None)
        long = request.query_params.get('long', None)
        if lat and long:
            point = self.create_point(lat, long)
            return queryset.distance(point, field_name='first_point__geom').order_by('distance')

        return queryset

    @staticmethod
    def create_point(latitude, longitude):
        try:
            point = GEOSGeometry(
                'POINT({long} {lat})'.format(long=longitude, lat=latitude), srid=4326
            )
        except ValueError:
            raise ValidationError(WRONG_LAT_LONG_TEXT)

        return point

    def to_html(self, request, queryset, view):
        return 'To order by distance use ?lat=10&long10 in url'
