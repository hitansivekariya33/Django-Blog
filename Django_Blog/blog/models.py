from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100,null=False)
    about_author = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    blog_pub_date = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField()

    class Meta:
        ordering = ['-blog_pub_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commented_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()

    def __str__(self):
        return self.comment_content
