from django.urls import path

from . import views

urlpatterns = [
    path('', views.shipperList.as_view()),
    path('create/', views.shipperCreate.as_view()),
    path('<int:pk>/', views.shipperDetail.as_view()),
    path('update/<int:pk>/', views.shipperUpdate.as_view()),
    path('delete/<int:pk>/', views.shipperDelete.as_view()),
]