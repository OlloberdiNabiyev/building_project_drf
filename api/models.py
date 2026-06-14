from django.db import models
from django.contrib.auth.models import User


class ConstructionCompany(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=155)
    address = models.TextField()
    count = models.IntegerField()
    company = models.ForeignKey(ConstructionCompany,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Comment(models.model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)