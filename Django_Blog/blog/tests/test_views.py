from django.test import TestCase
from blog.models import Author,Blog
from django.urls import reverse

class BlogListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 6
        for blog_num in range(number_of_blogs):
            blog_author = Author.objects.create(
                name = 'Jennifer Dasal',
                about_author = 'Jennifer Dasal is the curator of modern and contemporary art at the North Carolina Museum of Art in Raleigh, North Carolina, and the host of the independent podcast ArtCurious, which she started in 2016 and which was named one of the best podcasts by O, The Oprah Magazine and PC Magazine. She holds an MA in art history from the University of Notre Dame and a BA in art')
            
            Blog.objects.create(
                title = f'Test Blog {blog_num}',
                author = blog_author,
                blog_content = f'Test Blog {blog_num}')

    #The BlogListView (all-blog page) is accessible at the expected location (e.g./blog/blogs)
    def test_view_url_exists_at_desired_location(self): 
        response = self.client.get('/blog/blogs/') 
        self.assertEqual(response.status_code, 200)  

    #The BlogListView (all-blog page) is accessible at the expected named url (e.g.'blogs')
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    #The BlogListView (all-blog page) uses the expected template (e.g. the default)   
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    #The BlogListView pagination records by 5 (at least on the first page)
    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 5)           