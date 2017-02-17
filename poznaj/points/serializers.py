from rest_framework import serializers as drf_serializers
from rest_framework_gis import serializers

from poznaj.images.models import Image

from .models import Point


class PointSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Point
        geo_field = 'geom'
        fields = ('title', 'description', 'geom', 'images')
