from rest_framework import permissions, viewsets

from .models import Story
from .serializers import StorySerializer
from .filters import FirstPointFilter


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (FirstPointFilter,)
    ordering_fields = ('first_point',)
