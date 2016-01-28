from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = [
    url(r'^login/$', views.LoginList.as_view()),
    url(r'^login/(?P<pk>[0-9]+)/$', views.LoginDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)