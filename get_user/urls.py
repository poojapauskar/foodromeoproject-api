from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_user import views

urlpatterns = [
    #url(r'^my_profile/$', views.My_profileList.as_view()),
    url(r'^get_user/?activation_key=(?P<activation_key>(\w+))/$', views.Get_userDetail.as_view()),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]