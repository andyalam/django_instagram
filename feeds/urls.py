from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'^$', views.index, name='index'),
]