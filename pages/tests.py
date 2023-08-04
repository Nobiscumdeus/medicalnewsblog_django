from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_renders_correctly(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_home_uses_correct_template(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        
class SignupPageTest(TestCase):
    
    def setUp(self):
        self.username='username'
        self.email='username@email.com'
    def test_check_status_code(self):
        response=self.client.get('/accounts/signup/',200)
        self.assertEqual(response.status_code,200)
    def test_check_url_correct(self):
         response=self.client.get(reverse('signup'))
         self.assertEqual(response.status_code,200)
         self.assertTemplateused(response,'registration/signup.html')
         
    def test_sign_up_form(self):
        
        new_user=User.objects.create(
            self.username,self.email
        )
        self.assertEqual(User.objects.all().count(),1)
        self.assertEqual(User.objects.all()[0].username,self.username)
        self.assertEqual(User.objects.all()[0].email,self.email)
    
    
    
    
    
        
 
        
