from django.db import models

class Blog(models.Model):
    title = models.TextField()
    desc = models.TextField()
    content = models.TextField()
