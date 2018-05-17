# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
import pdb

# Create your views here.
class landingview(TemplateView):
    def get(self, request, **kwargs):
        # pdb.set_trace()
        return render(request, 'landing.html', context=None)

class signinview(TemplateView):
    def get(self,request, **kwargs):
        # pdb.set_trace()
        return render(request, 'signinaws.html', context=None)
class registration(TemplateView):
    def get(self,request, **kwargs):
        # pdb.set_trace()
        return render(request, 'Register.html', context=None)
