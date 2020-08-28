from django.db import models

class CV_Category(models.Model):
    name = models.TextField()
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CV_Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    position = models.IntegerField(default=0)
    CV_Category = models.ForeignKey(CV_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

