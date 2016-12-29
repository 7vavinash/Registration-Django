from django.conf.urls import url
from .views import home, signup, login_user, logout_user, UserDetails
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signup/', signup, name='signup'),
    url(r'^login/',login_user, name='login'),
    url(r'^logout/',logout_user, name='logout'),
    url(r'^userdetails/',UserDetails.as_view(), name='userdetails'),
]
