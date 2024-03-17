
from django.contrib import admin
from django.urls import path,include
# from django.contrib.staticfiles import 

from studyapp.settings import MEDIA_URL,STATIC_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))
]
# urlpatterns += staticfiles_urlpatterns(MEDIA_URL,STATIC_URL)
