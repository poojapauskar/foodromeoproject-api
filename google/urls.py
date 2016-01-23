from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from google import views

urlpatterns = [
    url(r'^google/$', views.CustomListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)