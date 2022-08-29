from re import template
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

#import api.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    #    path('api/', include(api.urls)),
    path('auth', include('djoser.urls')),
    path('auth', include('djoser.urls.jwt')),
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
