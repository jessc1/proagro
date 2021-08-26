from django.urls import path, include
from . import views



urlpatterns = [
    path('prod/list', views.ProdutorListAPIView.as_view(), name="produtor_lista"),
    path('prod/<int:id>/', views.ProdutorRetrieveAPIView.as_view(), name='produtor_detalhe'),
    path('prod/create', views.ProdutorCreateAPIView.as_view(), name='produtor_create'),
    path('prod/update/<int:id>/', views.ProdutorUpdateApiView.as_view(), name='produtor_update'),
    path('prod/delete/<int:id>/', views.ProdutorDeleteAPIView.as_view(), name='produtor_delete'),
   
     

    ]
