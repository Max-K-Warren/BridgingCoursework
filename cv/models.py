from django.db import models

class CV_Category(models.Model):
    name = models.TextField()
    position = models.IntegerField()

class CV_Item(models.Model):
    name = models.TextField()
    position = models.IntegerField()
    CV_Category = models.ForeignKey(CV_Category, on_delete=models.CASCADE)

