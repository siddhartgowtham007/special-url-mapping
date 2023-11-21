from app3.views import *

from django.urls import path

app_name='messages'

urlpatterns=[

    path('whatsapp/',whatsapp,name='whatsapp')
]