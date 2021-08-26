from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.shortcuts import render 
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import generics
from django.urls import reverse_lazy
from .models import Perda
from django.db.models import Q


class HomePageView(TemplateView):
    template_name='home.html'

class ProdutorPageView(ListView):
    model = Perda
    context_object_name = 'all_produtor'
    template_name = 'produtor_list.html'
    success_url = reverse_lazy('home')
     

class ProdutorDetailView(DetailView):
    model = Perda
    template_name = 'produtor_detail.html'

class ProdutorCreateView(CreateView):
    model = Perda
    template_name = 'novo_produtor.html'
    fields = '__all__'

class ProdutorDeleteView(DeleteView):
    model = Perda
    template_name = 'deletar_produtor.html'
    success_url = reverse_lazy('produtor_list')


class ProdutorUpdateView(UpdateView):
    model = Perda
    template_name= 'editar_produtor.html'
    fields = ['produtor_email','lavoura',]

class SearchResultsListView(ListView):
    model = Perda
    context_object_name = 'all_produtor'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Perda.objects.filter(
            Q(produtor_nome__icontains=query)|Q(produtor_cpf__icontains=query)

        )






