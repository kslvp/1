from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=100)
    price = models.ImageField(default=0) #cents

    def __str__(self):
        return self.name