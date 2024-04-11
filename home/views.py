from django.shortcuts import render
from django.views.generic import TemplateView

# Home page
class HomePage(TemplateView):
    template_name = 'home/index.html'