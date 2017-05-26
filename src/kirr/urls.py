from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView

from shortener.views import HomeView, URLRedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'), 
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
]
