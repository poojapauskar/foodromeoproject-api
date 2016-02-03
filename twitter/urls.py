from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from twitter import views

urlpatterns = [
    url(r'^twitter/$', views.CustomListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)