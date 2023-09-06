from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CreateBlog(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    summary = models.CharField(max_length=200,null=False,blank=False)
    post_date = models.DateField(auto_now_add=True)
    post_img = models.ImageField(null=True, upload_to='images/', blank=True)



    def __str__(self):
        return self.title + ' By ' + str(self.author)

class images (models.Model):
    logo_img = models.ImageField(null=True, upload_to='images/', blank=True)
    admin_img = models.ImageField(null=True, upload_to='images/', blank=True)

