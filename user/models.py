from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser,PermissionsMixin
# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self,name,email,Phone_Number,password=None):
        if not email:
            raise ValueError('must provide an email')
        if not Phone_Number:
            raise ValueError('must provide a number')
        
        user=self.model(
            email = self.normalize_email(email),
            Phone_Number = Phone_Number,
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,name,Phone_Number,password):
        user = self.create_user(
            email = self.normalize_email(email),
            Phone_Number = Phone_Number,
            name = name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(PermissionsMixin,AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True) 
    Phone_Number = models.CharField(max_length=10,unique=True,null=True)
    Department = models.ForeignKey('department.Department',on_delete=models.CASCADE,related_name='department',null=True,blank=True)
    Created_by = models.CharField(max_length=100)
    Created_at = models.DateTimeField(auto_now_add=True)
    Last_Updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    zendesk_id = models.CharField(max_length=100,null=True,blank=True)

    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['name','Phone_Number']
    
    objects=AccountManager()

    

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True