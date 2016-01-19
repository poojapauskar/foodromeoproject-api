from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from verify import views

urlpatterns = [
    url(r'^verify/$', views.VerifyList.as_view()),
    url(r'^verify/(?P<pk>[0-9]+)/$', views.VerifyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)