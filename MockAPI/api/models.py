from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Account(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Log(models.Model):
    request = models.CharField(max_length=1028)
    response = models.CharField(max_length=1018)
    date = models.DateTimeField(auto_now_add=True)


