from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from register import views

urlpatterns = [
    url(r'^register/$', views.RegisterList.as_view()),
    url(r'^register_detail/$', views.RegisterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)