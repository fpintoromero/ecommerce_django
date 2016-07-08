from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.view_index, name='home'),
	url(r'^category/(?P<slug>[\w-]+)/$', views.subcategory, name='subcategory'),
    url(r'^product/(?P<slug>[\w-]+)/$', views.product_detail, name='product_detail'),
]