from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_view/$', views.index, name='test_view'),

]