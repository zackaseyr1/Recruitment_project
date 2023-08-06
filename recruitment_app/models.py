from django.db import models

class JobApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    OCCUPATION_CHOICES = [
        ('nursing', 'Nursing'),
        ('software_engineer', 'Software Engineer'),
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('lawyer', 'Lawyer'),
        ('accountant', 'Accountant'),
        ('designer', 'Designer'),
        ('mechanic', 'Mechanic'),
        ('chef', 'Chef'),
        ('salesperson', 'Salesperson'),
        ('pilot', 'Pilot'),
        ('architect', 'Architect'),
        ('police_officer', 'Police Officer'),
        ('journalist', 'Journalist'),
        ('artist', 'Artist'),
        ('engineer', 'Engineer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    submission_date = models.DateTimeField(auto_now_add=True)
    application_id = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.application_id}"
