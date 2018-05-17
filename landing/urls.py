# landing/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from landing import views

urlpatterns = [
    url(r'^$', views.signinview.as_view(),name='signin'),
    url(r'^register', views.registration.as_view(),name='signin'),
    url(r'^landing', views.landingview.as_view(),name='landing'),
]
