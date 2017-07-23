from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^create/$', views.article_create, name="create"),
	url(r'^delete/$', views.article_delete, name="delete"),
]