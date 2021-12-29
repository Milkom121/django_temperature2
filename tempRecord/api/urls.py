from django.contrib import admin
from django.urls import path
from tempRecord.api.views import TempRecordCreateAPIView, TempRecordDetailAPIView



urlpatterns = [
    path('temperatures/' ,
         TempRecordCreateAPIView.as_view(),
         name='temperature-list'),

    path('temperatures/<int:pk>' ,
         TempRecordDetailAPIView.as_view(),
         name='room-temperature')
]









