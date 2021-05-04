from django.db import models
from restaurant.models import Restaurant
from django.core.validators import RegexValidator
from phone_field import PhoneField


# Create your models here.

guest = (
    ('', 'Choose...'),
    ('1', '1 Guest'),
    ('2', '2 Guests'),
    ('3', '3 Guests'),
    ('4', '4 Guests'),
    ('5+', '5+ Guests')
)


class Comment(models.Model):

    full_name = models.CharField(max_length=50)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length=254)
    content = models.TextField(max_length=250, blank=True, null=True)
    guest = models.CharField(max_length=50, null=True, choices=guest)

    created = models.DateTimeField(auto_now_add=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None, null=True)