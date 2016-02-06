from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from verify import views

from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet


urlpatterns = [
    url(r'^verify/$', views.VerifyList.as_view()),
    url(r'^verify/(?P<pk>[0-9]+)/$', views.VerifyDetail.as_view()),
    url(r'^device/apns/?$', APNSDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_apns_device'),
]

urlpatterns = format_suffix_patterns(urlpatterns)