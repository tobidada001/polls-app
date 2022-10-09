from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('add/', views.addpoll, name='add'),
    path('cancelpoll/', views.cancelpoll, name= 'cancelpoll'),
    path('chooseoption/<int:pk>', views.choose, name= 'choose'),
    path('details/<int:prim>', views.details, name='details')
]
