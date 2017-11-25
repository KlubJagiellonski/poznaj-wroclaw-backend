from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'mobile/about.html'

class ClubView(TemplateView):
    template_name = 'mobile/club.html'

class TeamView(TemplateView):
    template_name = 'mobile/team.html'

class PartnersView(TemplateView):
    template_name = 'mobile/partners.html'
