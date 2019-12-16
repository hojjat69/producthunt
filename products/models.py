from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#title, url, pub date, votes_total, image, icon, body, pubdatepretty, hunter

class Products(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/images/')
    votes_total = models.IntegerField(default=1)
    icon =models.ImageField(upload_to='media/icons/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1500)
    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y ')
    def summary (self):
        return self.body[:200]
    def __str__(self):
        return self.title
    




