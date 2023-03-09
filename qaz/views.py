from django.shortcuts import render
from django.views.generic import TemplateView
from qaz.models import Clothes


class ClothesViews(TemplateView):
    template_name = 'index.html'

