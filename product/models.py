from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "title")    
    url = models.TextField()
    pub_date = models.DateTimeField(verbose_name = "date of publication", null = True, default = None, blank = True)
    votes_total = models.IntegerField(verbose_name="total votes", default=0)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")