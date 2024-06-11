from django.db import models

# Create your models here.


class Jobportal(models.Model):
    name    = models.CharField(max_length=250)
    job     = models.CharField(max_length=250)
    date    = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
#  Company Dashboard

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



# UserDashboard

class UserDashboard(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class UserProfiles(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class UserActivityTracking(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class UserSuspension(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class UserFeedback(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


# Job Management

class JobApplicationTracking(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class JobCategoryManagement(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class JobListingDashboard(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class JobPostingEditing(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class JobStatusManagement(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    