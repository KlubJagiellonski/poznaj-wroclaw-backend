from django.conf.urls import url

from .views import AboutView, ClubView, TeamView, PartnersView

urlpatterns = [
    url(r'^about/$', AboutView.as_view()),
    url(r'^club/$', ClubView.as_view()),
    url(r'^team/$', TeamView.as_view()),
    url(r'^partners/$', PartnersView.as_view()),
]
