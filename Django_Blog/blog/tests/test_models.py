from django.test import TestCase
from blog.models import Author,Blog,Comment

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Jennifer Dasal',about_author = 'Jennifer Dasal is the curator of modern and contemporary art at the North Carolina Museum of Art in Raleigh, North Carolina, and the host of the independent podcast ArtCurious, which she started in 2016 and which was named one of the best podcasts by O, The Oprah Magazine and PC Magazine. She holds an MA in art history from the University of Notre Dame and a BA in art')
        
    #testcase for check author name label 
    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')
    
    #testcase for check author biography label 
    def test_about_author_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('about_author').verbose_name
        self.assertEqual(field_label,'about author')

    #testcase for check author name maximum length
    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length,100)

    #testcase for check author object name
    def test_object_name(self):
        author = Author.objects.get(id=1)
        get_object_name = author.name
        self.assertEqual(get_object_name,str(author))

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name='Jennifer Dasal',about_author = 'Jennifer Dasal is the curator of modern and contemporary art at the North Carolina Museum of Art in Raleigh, North Carolina, and the host of the independent podcast ArtCurious, which she started in 2016 and which was named one of the best podcasts by O, The Oprah Magazine and PC Magazine. She holds an MA in art history from the University of Notre Dame and a BA in art')
        Blog.objects.create(title='Test Blog', author=author ,blog_content='This is a test blog.')

    #testcase for check get_absolute_url return expected url 
    def test_get_absolute_url(self):
        blog=Blog.objects.get(id=1)       
        self.assertEquals(blog.get_absolute_url(),'/blog/blogs/1/')

    #testcase for check blog title label 
    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    #testcase for check blog content label
    def test_blog_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('blog_content').verbose_name
        self.assertEqual(field_label, 'blog content')
    
    #testcase for check title maximum length 
    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length,100)
    
    #testcase for check blog object name
    def test_object_name(self):
        blog = Blog.objects.get(id=1)
        get_object_name = blog.title
        self.assertEqual(get_object_name,str(blog))

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name='Jennifer Dasal', about_author = 'Jennifer Dasal is the curator of modern and contemporary art at the North Carolina Museum of Art in Raleigh, North Carolina, and the host of the independent podcast ArtCurious, which she started in 2016 and which was named one of the best podcasts by O, The Oprah Magazine and PC Magazine. She holds an MA in art history from the University of Notre Dame and a BA in art')
        blog = Blog.objects.create(title='Test Blog', author=author, blog_content='This is a test blog.')
        Comment.objects.create(comment_content='Good', blog=blog)

    #testcase for check comment content label
    def test_comment_content_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_content').verbose_name
        self.assertEqual(field_label, 'comment content')

    #testcase for check comment content object name
    def test_object_name(self):
        comment = Comment.objects.get(id=1)
        get_object_name = comment.comment_content
        self.assertEqual(get_object_name,str(comment))