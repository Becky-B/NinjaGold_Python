from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path("Farm", views.Farm),
    path('Casino', views.Casino),
    path('House', views.House),
    path('Cave', views.Cave),
    path('reset', views.reset)
]