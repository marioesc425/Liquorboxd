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