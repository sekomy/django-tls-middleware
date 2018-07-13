# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View


class TestView(View):
    def get(self, *args):
        return HttpResponse('Response')

