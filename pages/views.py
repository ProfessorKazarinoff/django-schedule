# pages/views.py

from django.views.generic import TemplateView, ListView
from schedules.models import Instructor


class AboutPageView(TemplateView):
    template_name = "about.html"


class HomePageView(ListView):
    model = Instructor
    template_name = "home.html"
