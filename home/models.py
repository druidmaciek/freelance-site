from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User,
                               related_name='posts',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    status = models.CharField(max_length=5, choices=(
        ('live', 'Live'),
        ('draft', 'Draft'),
    ), default='draft')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # TODO auto-create slug based on title
    # TODO add published manager
    # TODO add SEO fields

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    company = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=120, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.first_name} {self.last_name}'
