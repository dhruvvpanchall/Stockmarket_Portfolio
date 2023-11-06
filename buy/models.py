from django.db import models

# Create your models here.
class Stock(models.Model):
    Stock=models.CharField(max_length=20)
    Open =models.DecimalField(max_digits=6,decimal_places=2)
    Close=models.DecimalField(max_digits=6,decimal_places=2)
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self) :
        return self.Stock

