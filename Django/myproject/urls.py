from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('myapp.urls')),
    url(r'^blog/', include('myapp.urls')),
    url(r'^', include('myapp.urls')),
    #url(r'^auth/login/$', include('myapp.urls')),
]