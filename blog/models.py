from django.db import models
from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    head0 =models.CharField(max_length=500,default="")
    chhead0 =models.CharField(max_length=5000,default="")
    head1 =models.CharField(max_length=500,default="")
    chhead1 =models.CharField(max_length=5000,default="")
    head2 =models.CharField(max_length=500,default="")
    chhead2 =models.CharField(max_length=5000,default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title
