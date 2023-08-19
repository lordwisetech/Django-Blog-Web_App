from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CreateBlog(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' By ' + str(self.author)
