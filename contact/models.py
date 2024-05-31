from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.TextField()
    number = models.CharField(max_length=212)
    email = models.EmailField()
    business_hours = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

