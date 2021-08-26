from django.db import models
from django.urls import reverse

class Perda(models.Model):
      
    EVENTO_CHOICES = (('I', 'CHUVA EXCESSIVA'),
                      ('II', 'GEADA'),
                      ('III', 'GRANIZO'),
                      ('IV', 'SECA'),
                      ('V', 'VENDAVAL'),
                      ('VI', 'RAIO'),)
                      

    TIPO_LAVOURA_CHOICES = (('milho', 'milho'),
                             ('soja', 'soja'),
                             ('trigo', 'trigo'),
                             ('feijao', 'feijão'),
                             ('outro', 'outro'),)
                                  
    produtor_nome = models.CharField (max_length=50,help_text = "Nome do produtor rural")
    produtor_email = models.EmailField(help_text ="E-mail do produtor")
    produtor_cpf = models.CharField(max_length=20,verbose_name = "CPF do produtor rural")
    produtor_data_colheita = models.DateTimeField(auto_now= False, null=True, blank=True)
    evento = models.CharField(max_length=30, choices=EVENTO_CHOICES,
                               null=True, blank=False)
    lavoura = models.CharField(max_length=30, choices=TIPO_LAVOURA_CHOICES,
                              null=True, blank=False)


    def __str__(self):
        """___str___."""
        return self.produtor_nome

    def get_absolute_url(self):
        #return reverse('produtor_list')
        return reverse('produtor_detail',args=[str(self.id)])
    
    
