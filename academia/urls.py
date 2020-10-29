from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeacademia,name='homeacademia'),
    path('django/',views.djangotuto,name='django'),
]