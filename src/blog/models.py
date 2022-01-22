from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
