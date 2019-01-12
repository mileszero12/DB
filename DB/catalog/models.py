from django.db import models

# Create your models here.
class FoodType(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    typeName = models.CharField(
        max_length=200,
        help_text="Enter a food type name:"
        )
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.typeName

class Food(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    foodName = models.CharField(
        max_length=200,
        help_text="Enter a food name:"
        )
    price = models.CharField(
        max_length=200,
        help_text="Enter a food price:"
        )
    typeID = models.ForeignKey('FoodType', on_delete = models.CASCADE, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.foodName