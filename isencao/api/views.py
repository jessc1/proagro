from rest_framework import generics
from .serializers import ProdutorListSerializer, ProdutorDetailSerializer
#from ..views import ProdutorPageView, ProdutorDetailView, ProdutorCreateView, ProdutorDeleteView, ProdutorUpdateView
from ..models import Perda


class ProdutorListAPIView(generics.ListAPIView):
    """
    Retorna uma lista de todos os produtores
    cadastrados.
    """
    queryset = Perda.objects.all()
    serializer_class = ProdutorListSerializer

class ProdutorRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retorna os dados sobre um produtor
    """
    lookup_field = "id"
    queryset = Perda.objects.all()
    serializer_class = ProdutorDetailSerializer

class ProdutorCreateAPIView(generics.CreateAPIView):
    """
    Cria um novo produtor na API.
    """    
      
    queryset = Perda.objects.all()
    serializer_class = ProdutorDetailSerializer    


class ProdutorUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    Atualize ou edita os dados sobre um produtor
    """
    lookup_field = "id"
    queryset = Perda.objects.all()
    serializer_class = ProdutorDetailSerializer

class ProdutorDeleteAPIView(generics.DestroyAPIView):
    """
    Deleta um produtor na API
    """

    lookup_field = "id"
    queryset = Perda.objects.all()



    

    
