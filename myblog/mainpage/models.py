from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False)
    body = models.TextField()

    def _str_(self):
        return self.title