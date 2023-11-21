from app2.views import *

from django.urls import path

app_name='stories'

urlpatterns=[

    path('facebook/',facebook,name='facebook')
]