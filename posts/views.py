# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
	post_list = Post.objects.all()
	first_post = Post.objects.first()
	context = {
	
	"user" : request.user,
	"list" : post_list,
	"first" : first_post

	}
	return render(request, 'create.html', context)


def post_update(request):
	return HttpResponse("<h1> Update </h1>")

def post_delete(request):
	return HttpResponse("<h1> Delete </h1>")

def post_list(request):
	return HttpResponse("<h1> List </h1>")

def post_detail(request): 
	return HttpResponse("<h1> Detail </h1>")

def post_save(request):
	return HttpResponse("<h1> Save </h1>")

def post_time(request):
	return HttpResponse("<h1> Time </h1>")

def post_tag(request):
	return HttpResponse("<h1> Tag </h1>")