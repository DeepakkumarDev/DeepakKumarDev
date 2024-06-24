from django.db import models

# Create your models here.
# models.py

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    occupation = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
