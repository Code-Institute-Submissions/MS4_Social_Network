from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class DonationView(TemplateView):
    template_name = 'dontaion.html'
