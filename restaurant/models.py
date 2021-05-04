from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.contrib.auth.models import User


# Create your models here.

cuisine_choice = (
    ('', 'Choose...'),
    ('American', 'American'),
    ('European', 'European'),
    ('French', 'French'),
    ('Mexican', 'Mexican'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Latin', 'Latin American'),
)

capacity_choice = (
    ('', 'Choose...'),
    ('100', '100'),
    ('75', '75'),
    ('50', '50'),
    ('25', '25'),
    ('10', '10'),
)

state = (
    ('', 'Choose...'),
    ('CA', 'California'),
    ('NY', 'New York'),
    ('IL', 'Chicago')
)

status = (
    ('', ''),
    ('Available', 'Vacant'),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    cuisine = models.CharField(max_length=50, blank=True, null=True, choices=cuisine_choice)
    live_capacity = models.CharField(max_length=50, blank=True, null=True, choices=capacity_choice)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True, choices=state)
    zipcode = models.CharField(max_length=50, blank=True, null=True)

    image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)
    detail_main = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640, 480)],
        format="jpeg",
        options={"quality": 80}
    )

    facebook = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)

    lunch9 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    lunch10 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    lunch11 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    lunch12 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    lunch1 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    lunch2 = models.CharField(max_length=50, blank=True, null=True, choices=status)

    dinner5 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    dinner6 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    dinner7 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    dinner8 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    dinner9 = models.CharField(max_length=50, blank=True, null=True, choices=status)
    dinner10 = models.CharField(max_length=50, blank=True, null=True, choices=status)


    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name