from django.urls import path,include
from rest_framework import views
from .views import *
from . import views
from django.db import router
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("base1",views.BaseAPI,basename='Basetable')
urlpatterns = [
     path('', include(router.urls)),
   
     path('base/', PostAPI.as_view()),
     path('base/<int:base_id>/', PostAPI.as_view()),

     path('product/', PropertiesAPI.as_view()),
     path('product/<int:product_id>/', PropertiesAPI.as_view()),

     path('dimension/', DimensionsAPI.as_view()),
     path('dimension/<int:id>/', DimensionsAPI.as_view()),

     path('images/', ImagesAPI.as_view()),
     path('images/<int:id>/', ImagesAPI.as_view()),

    # path('productapi/', ProductAPI.as_view()),
    #path('productapi/<int:product_id>/', ProductAPI.as_view()),


    
    

]


 