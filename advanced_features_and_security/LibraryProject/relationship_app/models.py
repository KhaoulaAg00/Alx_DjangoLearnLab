# from django.db import models
# django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# # Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title

# class Library(models.Model):
#         name = models.CharField(max_length=100)
#         books = models.ManyToManyField(Book)

#         def __str__(self):
#             return self.name
        
# class Librarian(models.Model):
#     name = models.CharField(max_length=100)
#     library = models.OneToOneField(Library, on_delete=models.CASCADE)  

#     def __str__(self):
#         return self.name
    
# class UserProfile(models.Model):
#      user = models.OneToOneField(User, on_delete=models.CASCADE)



#      Role_Choices =(
#         ('Admin','Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
    
#     )
    
# role = models.CharField(max_length=50,  choices='Role_Choices')
# userprofile = models.TextField()

# def __str__(self):
#     return f'{self.user.username} - {self.role}'

# #Signal to automatically create a UserProfile when a new User is created
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()    

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    
    def __str__(self):
        return f"{self.title} by {self.author}"  

#Extending Book Model with Custom Permissions
    class BookPermissions(models.Model):
        Permissions_Choices =(
            ('can_add_book', 'can_add_book'),
            ('can_change_book', 'can_change_book'),
            ('can_delete_book', 'can_delete_book'),

        )
    permissions = models.CharField(max_length=50,  choices='Permissions_Choices')
    meta = models.TextField()
    
    def __str__(self):
        return f'{self.permissions}'
    
    class Meta:
        ordering = ['permissions']
        verbose_name = 'Book Permission'
        verbose_name_plural = 'Book Permissions'


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name   

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
    
#Extending User Model with a UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    Role_Choices =(
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    
    )

role = models.CharField(max_length=50,  choices='Role_Choices')
userprofile = models.TextField()

def __str__(self):
    return f'{self.user.username} - {self.role}'

#Signal to automatically create a UserProfile when a new User is created
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(User=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL )
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models custom user manager 
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'profile_photo']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
