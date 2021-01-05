from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUser (AbstractUser) :
    USER_ROLE = (
        ('1', 'hr'),
        ('2', 'user'),
        ('3', 'admin'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ID_TYPE = (
        ('National id', 'National id'),
        ('Passport', 'Passport'),
    )
    SOCIAL_STATUS = (
        ('Married', 'Married'),
        ('single', 'single'),
    )

    email = models.EmailField(max_length = 100,
        blank=True,
        null=True,)
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length = 100)
    nationality = models.CharField(max_length=15)
    id_type = models.CharField(max_length=15, choices=ID_TYPE)
    id_num = models.CharField(max_length=15)
    hire_date = models.DateField('HireDate',
        blank=True,
        null=True,)
    social_status = models.CharField(max_length=15, choices=SOCIAL_STATUS)
    emp_unm = models.CharField(max_length=15)
    date_of_birth = models.DateField('Date Of Birth',
        blank=True,
        null=True,)
    place_of_birth = models.CharField(max_length = 50)
    mobile_num = models.CharField(max_length = 11)
    insured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_medical = models.BooleanField(default=False)
    balance = models.IntegerField(
        default=21,
        blank=True,
        null=True,
         )
    role = models.CharField(max_length=1,
    choices=USER_ROLE,
    default='2'
    )      


    def __str__(self):
        return self.username

