from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Perda

class PerdaTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.perda = Perda.objects.create(
            produtor_nome='Obi wan',
            produtor_email='obiwan@email.com',
            produtor_cpf ='40157121120',
            produtor_data_colheita='2021-08-21',
            evento='GEADA',
            lavoura='soja',
                  
        )
    def test_get_absolute_url(self):
        self.assertEqual(self.perda.get_absolute_url(),'/produtor/2/')


    def test_post_produtor(self):
        self.assertEqual(f'{self.perda.produtor_nome}', 'Obi wan')
        self.assertEqual(f'{self.perda.produtor_email}', 'obiwan@email.com')
        self.assertEqual(f'{self.perda.produtor_cpf}', '40157121120')


    def test_produtor_list_view(self):
        response = self.client.get(reverse('produtor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Obi wan')
        self.assertTemplateUsed(response, 'produtor_list.html')


    def test_produtor_create_view(self):
        response =self.client.post(reverse('novo_produtor'), {
            'produtor_nome':'Obi wan',
            'produtor_email':'obiwan@email.com',
            'produtor_cpf' :'40157121120',
            'produtor_data_colheita':'2021-08-21',
            'evento':'GEADA',
            'lavoura':'soja',
        })
        
        self.assertContains(response, 'Obi wan')

        
    def test_produtor_detail_view(self):
        response= self.client.get('/produtor/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produtor_detail.html')

    def test_produtor_update_view(self): 
        response = self.client.post(reverse('editar_produtor', args='2'), {
            'produtor_email': 'kenobi@email.com',
            'lavoura': 'soja',
        })
        self.assertEqual(response.status_code, 302)
        
        

   
