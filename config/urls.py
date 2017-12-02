from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from poznaj.images.views import ImagesViewSet
from poznaj.points.views import PointsViewSet
from poznaj.stories.views import StoriesViewSet

from poznaj.views import MainView

router = routers.DefaultRouter()
router.register(r'images', ImagesViewSet)
router.register(r'points', PointsViewSet)
router.register(r'stories', StoriesViewSet)

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^$', MainView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^health/', include('health_check.urls')),
    url(r'^mobile/', include('poznaj.mobile.urls')),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
