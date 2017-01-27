from rest_framework import viewsets, permissions

from .models import Point
from .serializers import PointSerializer


class PointsViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
