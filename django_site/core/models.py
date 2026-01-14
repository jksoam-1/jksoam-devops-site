from django.db import models


class Page(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('devops', 'DevOps'),
        ('blogs', 'Blogs'),
    ]

    page_name = models.CharField(max_length=20, choices=PAGE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)

    def __str__(self):
        return self.page_name


class HomeImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/')
    link = models.CharField(
        max_length=50,
        choices=[
            ('/devops/', 'DevOps'),
            ('/blogs/', 'Blogs'),
        ]
    )

    def __str__(self):
        return self.title


# 🔥 NEW MODEL FOR BLOGS
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()   # 1000+ words supported
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
