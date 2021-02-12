from django.db import models

# Create your models here.

WILLINGNESS_CHOICES = [
    ('YES','Yes'),
    ('NO','No'),
    ('MAYBE','May be')
]


class RegisteredUser(models.Model):
    email_address = models.EmailField(max_length=254,unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(max_length=30)
    country_of_residence = models.CharField(
        max_length=30,
        blank=True
    )
    contact_number = models.CharField(max_length=20,
        blank=True
    )
    willingness_to_join_session = models.CharField(
            max_length=10,
            choices=WILLINGNESS_CHOICES,
            blank=True
    )
    comments = models.TextField(default='None',blank=True)
    registered_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name+" Email:"+self.email_address

