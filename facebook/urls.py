from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from facebook import views

urlpatterns = [
    url(r'^facebook/$', views.CustomListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)