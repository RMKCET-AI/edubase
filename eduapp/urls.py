from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('material', views.material, name='material'),
    path('material/ai',views.ai,name='material_ai'),
    path('material/cse',views.cse,name='material_cse'),
    path('material/ece',views.ece,name='material_ece'),
    path('material/mech',views.mech,name='material_mech'),
]
