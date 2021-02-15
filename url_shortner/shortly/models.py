from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Connection(models.Model):
    redirect_url=models.URLField(max_length=1500)
    slug=models.CharField(max_length=50)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.slug)