from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import PermissionDenied

STATUS = ((0, "Believer"),(1, "Non-Believer"))
    
class User(BaseUserManager):
        is_admin = models.BooleanField(default=False)

        
        def __str__(self):

            return self.is_admin
    
class Admin(models.Model):
    user = models.CharField(max_length=100)

    firstName = models.CharField(max_length=100)

    surName = models.CharField

    email = models.EmailField()

    password = models.CharField(max_length=100)

    phone = models.CharField(max_length=100)

    contactAddress = models.CharField(max_length=100)

    gender = models.CharField(max_length=100)

    dateOfBirth = models.DateField()

    status = models.IntegerField(choices = STATUS, default=0)

    occupation = models.CharField(max_length=100)

    education = models.CharField(max_length=100)

    adminRole = models.CharField(max_length=100)

    adminDepartment=models.CharField(max_length=50)


    def __str__(self):

        return f"{self.firstName} on '{self.adminDepartment}'" 

class Permission(models.Model):

    user = models.CharField(max_length=100)
    
    adminRole=models.ForeignKey(Admin, on_delete=models.CASCADE)

    designatedPermission = models.CharField(max_length=100)

    def permission(User):
        if not User.is_admin:
            raise PermissionDenied
        return True



class Clients(models.Model):
    user=models.CharField(max_length=100)

    firstName = models.CharField(max_length=100)

    surName = models.CharField

    phone = models.CharField(max_length=100)

    contactAddress = models.CharField(max_length=100)

    gender = models.CharField(max_length=100)

    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.userName   
        

class Authentication(models.Model):

    user=models.CharField(max_length=100)

    signIn=models.CharField(max_length=50)

    signOut=models.CharField(max_length=50)

    register=models.CharField(max_length=50)

    on_delete=models.BooleanField(default=False)

    clients=models.ForeignKey(Clients, on_delete=models.CASCADE)

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
     

    def __str__(self):

        return self.signIn 


class About(models.Model):
        
        clients=models.CharField(max_length=100)

        email = models.CharField(max_length=50)

        dateofbirth =models.DateTimeField(max_length=25)

        marital_status =models.BooleanField(default=False)

        occupation = models.CharField(max_length=25)

        education = models.CharField(max_length=50)

        def __str__ (self):
            return  self.education


    

