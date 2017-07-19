from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from rainreport import views
from django.views.generic.base import RedirectView

urlpatterns = [ 
    url(r'^rainfall/$', views.RainfallList.as_view()),
    url(r'^rainfall/(?P<pk>[0-9]+)/$', views.RainfallDetail.as_view()),
    url(r'^stations$', views.StationList.as_view()),
    # url(r'^stations/(?P<county>.+)/$', views.StationList.as_view()),
    url(r'^.*$', views.RainfallList.as_view(), name='rainfall_list')
]
                                         
urlpatterns = format_suffix_patterns(urlpatterns)
