from django.db import models

class Member (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True)
    joined_time = models.DateField(blank=True)

    def __str__ (self):
        return f'{self.firstname}- {self.lastname}'
