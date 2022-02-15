from django.conf.urls import url
from basicapp import views

app_name='zico'
urlpatterns=[

    url(r'^register/$',views.register,name='register'),
    url(r'^$',views.base),
    url(r'^login/$',views.userlogin,name='userlogin')


]
