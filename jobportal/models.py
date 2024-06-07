from django.db import models

# Create your models here.


class Jobportal(models.Model):
    name    = models.CharField(max_length=250)
    job     = models.CharField(max_length=250)
    date    = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class CompanyDashboard(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class CompanyProfiles(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class CompanyActivityTracking(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class CompanySuspension(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class CompanyFeedback(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
