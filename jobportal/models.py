from django.db import models

# Create your models here.


class Jobportal(models.Model):
    name         = models.CharField(max_length=250)
    Job_name     = models.CharField(max_length=250)
    date         = models.DateField(auto_now=True)

    def __str__(self):
        return self.name