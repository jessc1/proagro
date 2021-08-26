from django.urls import path
from .views import (
    ProdutorPageView,
    ProdutorDeleteView,
    ProdutorUpdateView,
    ProdutorCreateView,
    ProdutorDetailView,
    SearchResultsListView,
    HomePageView,
)


urlpatterns = [
    path('produtor/lista', ProdutorPageView.as_view(), name='produtor_list'),
    path('produtor/<int:pk>/deletar/',ProdutorDeleteView.as_view(), name='deletar_produtor'),
    path('produtor/<int:pk>/editar/',ProdutorUpdateView.as_view(), name='editar_produtor'),
    path('produtor/novo/',ProdutorCreateView.as_view(), name='novo_produtor'),
    path('produtor/<int:pk>/',ProdutorDetailView.as_view(), name='produtor_detail'),
    path('produtor/search/', SearchResultsListView.as_view(), name='search_results'),
    path('',HomePageView.as_view(), name='home'),
]
