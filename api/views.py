from rest_framework import generics, filters
from .serializers import ProdutorListSerializer, ProdutorDetailSerializer
from isencao.models import Perda


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



class ProdutorUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Atualiza os dados de um hóspede na API.
    """
        
    lookup_field = "id"
    queryset = Perda.objects.all()
    serializer_class = ProdutorDetailSerializer

class ProdutorCreateAPIView(generics.CreateAPIView):
    """
    Cria um novo Produtor na API.
    """    
      
    queryset = Perda.objects.all()
    serializer_class = ProdutorDetailSerializer

class ProdutorDeleteAPIView(generics.DestroyAPIView):
    """
    Deleta um produtor na API
    """

    lookup_field = "id"
    queryset = Perda.objects.all()



    

    
