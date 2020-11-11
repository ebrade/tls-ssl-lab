from django.conf.urls import url
from django.urls import path
from .views import ContactView, home, signup, login_request, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('contact/', ContactView, name="contactus"),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login_request, name='login'),
    url(r'^logout', logout_view, name='logout'),
]
