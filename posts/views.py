# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def post_list(request):
	obj_list = Post.objects.all()
	
	context = {
	
	
	"post_list" : obj_list,
	
	

	}
	return render(request, 'post_list.html', context)





def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id) 
	context= {
	"instance": obj,
	}


	return render(request, 'post_detail.html', context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "You created an object!!")
		return redirect("posts:list")
	context ={
		"form" : form,
	}
	return render(request, 'post_create.html', context)


def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Are you sure?")
		return redirect("posts:list")
	context ={
		"form" : form,
		"post_object": post_object,
	}
	return render(request, 'post_update.html', context)
def post_delete(request, post_id):
	obj= Post.objects.get(id=post_id).delete()
	messages.warning(request, "really???")
	return redirect("posts:list")





