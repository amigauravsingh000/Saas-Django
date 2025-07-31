from django.db import models

# Create your models here.

class PageVisit(models.Model):
    #db -> Table
    #id -> hidenn primary key --> autofield -> 1, 2, 3, 4, 5, 6 .....
    path = models.TextField(blank=True, null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col

