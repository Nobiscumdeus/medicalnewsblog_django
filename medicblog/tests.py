from django.test import TestCase
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse
from django.conf import settings 
#User=settings.AUTH_USER_MODEL

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self)->None: #This are to set up the functionality that will be used within the rest of the class
       self.user=get_user_model().objects.create_user(
           username='testuser',
           email='test@gmail.com',
           password='testpassword##'
           
       )
       self.post=Post.objects.create(
           title='Romantic Doctor',
           body='The Romantic doctor is Doctor Kim',
           author=self.user
           
        )
    def test_assert_title_is_string(self):
        post_title=Post(title='A sample')
        #self.assertEqual(str(post_title),post_title.title)
        
        
    def test_content_of_post(self):
        #self.asssertEqual(f'{self.post.title}', 'Romantic Doctor')
        self.assertEqual(f'{self.post.body}', 'The Romantic doctor is Doctor Kim')
        self.assertEqual(f'{self.post.author}', f'{self.post.author}')
        
    def test_post_list_views_correct(self):
        response=self.client.get('/medicblog/post')
        self.assertEqual(response.status_code,200)
        #self.assertContains(response,self.post.title)
        self.assertTemplateUsed(response,'medicblog/list.html')
        
    '''
     def test_post_list_details_correctly(self):
        response=self.client.get('/medicblog/post/1/')
        self.assertEqual(response.status_code,200)
        #self.assertContains(response,'Romantic Doctor')
        self.assertTemplateUsed(response,'medicblog/detail.html')
    '''
   
        
    def test_get_absolute_url_correctly(self):
        self.assertEqual(self.post.get_absolute_url(),'/medicblog/post/1/')
        
    def test_get_content_of_post_correctly(self):
        self.assertEqual(f'{self.post.title}','Romantic Doctor')
        self.assertEqual(f'{self.post.body}','The Romantic doctor is Doctor Kim')
        self.assertEqual(f'{self.post.author}',f'{self.post.author}')
    def test_list_view_correct(self):
        response=self.client.get(reverse('medicblog:list'))
        self.assertEqual(response.status_code,200)
        #self.assertContains(response,'Romantic Doctor')
        self.assertTemplateUsed(response,'medicblog/list.html')
    '''
    def test_detail_view_correct(self):
        response=self.client.get(reverse('medicblog:detail',args='1'))
        self.assertEqual(response.status_code,200)
        #self.assertContains(response,'Romantic Doctor')
        self.assertTemplateUsed(response,'medicblog/detail.html')
    '''    
    
        
    def test_create_view_correct(self):
        response=self.client.post(reverse('medicblog:create'),{
            'title':'Blog Title',
            'body':'New Blog Title',
            'author':self.user.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,'Romantic Doctor')
        self.assertEqual(Post.objects.last().body,'The Romantic doctor is Doctor Kim')
        
    def test_update_view_correct(self):
        response=self.client.post(reverse('medicblog:update',args='1'),{
            'title':'updated title',
            'body':'updated body'
            
        })
        self.assertEqual(response.status_code,302)
        
    def test_delete_view_correct(self):
        response=self.client.post(reverse('medicblog:delete',args='1'))
        self.assertEqual(response.status_code,302)
        
        
        
        
        
        
        
        
        
        
        

