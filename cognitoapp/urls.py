from django.conf.urls import url
from .import views
from views import  *
urlpatterns=[
    # url(r'^login/',views.login,name='login'),
    # url(r'^activate/',views.activate,name='activate'),
    # url(r'^logout/',views.logout,name='logout'),

    url(r'^activate/$', ActivateView.as_view()),
    url(r'^login/$', LoginView.as_view(),name="sucess")
]