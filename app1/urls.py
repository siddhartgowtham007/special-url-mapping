from app1.views import *

from django.urls import path

app_name='posts'

urlpatterns=[

    path('insta/',insta,name='insta')
]