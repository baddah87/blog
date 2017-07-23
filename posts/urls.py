from django.conf.urls import url

# put . instead of posts if i am in the same file#

from . import views

urlpatterns = [
	url(r'^create/$', views.post_create, name="create"),
    url(r'^update/$', views.post_update, name="update"),
    url(r'^delete/$', views.post_delete, name="delete"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^detail/$', views.post_detail, name="detail"),
    url(r'^save/$', views.post_save, name="save"),
    url(r'^time/$', views.post_time, name="time"),
    url(r'^tag/$', views.post_tag, name="tag"),
]