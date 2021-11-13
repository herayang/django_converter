from django.urls import path
from converter import views

urlpatterns = [
    path('', views.converter, name='conTemp'),
    path('conLen',views.len_convert,name="conLen"),
    path('conVol',views.vol_convert,name="conVol")
]