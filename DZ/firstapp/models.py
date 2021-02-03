from django.db import models


class PhoneBrand(models.Model):
    Brand = models.CharField(max_length=30)
    Site = models.CharField(max_length=50)
    Subscrprice = models.IntegerField()

    def __str__(self):
        return self.Brand


class Phone(models.Model):
    PhoneBrand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    prise = models.IntegerField()
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name
