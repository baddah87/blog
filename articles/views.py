# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def article_create(request):
	return render(request, 'write.html', {})

def article_delete(request):
	return HttpRespone("<h1> Delete </h1>")