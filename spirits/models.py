from django.contrib.auth.models import User
from django.db import models

# Create your models here.

##Create Category Class
class Category(models.TextChoices):
    ## The first is the stored database value, the second is the human-readable label shown in forms/admin.
    WHISKEY = "Whiskey", "Whiskey"
    VODKA = "Vodka", "Vodka"
    RUM = "Rum", "Rum"
    TEQUILA = "Tequila", "Tequila"
    GIN = "Gin", "Gin"

##Create Spirit Class
class Spirit(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length=20, choices=Category.choices)
    brand = models.CharField(max_length = 50)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = [
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
    (3.5, '3.5'),
        (4, '4'),
        (4.5, '4.5'),
        (5, '5'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spirit = models.ForeignKey(Spirit, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=RATING_CHOICES)
    text = models.TextField(blank=True)
    date_tried = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"{self.spirit.name} review by {self.user.username}"


