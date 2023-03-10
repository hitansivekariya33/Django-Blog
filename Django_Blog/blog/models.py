from django.db import models
from django.urls import reverse
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Author(models.Model):
    name = models.CharField(max_length=100,null=False)
    about_author = models.TextField()

    def __str__(self):
        return self.name

class Blog(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=100)
    blog_content = models.TextField()

    def __str__(self):
            return f'{self.title}' + f'{self.blog_content}' 

    def get_absolute_url(self):
        return reverse("blogdetail", kwargs={"pk": self.pk})
    
class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    comment_content = models.TextField()

    def __str__(self):
        return self.comment_content    