from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hello_world),
	url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail)
]