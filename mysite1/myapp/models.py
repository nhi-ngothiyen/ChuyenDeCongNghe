from django.db import models
from datetime import date

# Nhạc sĩ
class Musician(models.Model):
    class Instrument(models.TextChoices):
        GUITAR = "G", "Guitar"
        DRUMS = "D", "Drums"
        PIANO = "P", "Piano"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=1, choices=Instrument)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Album
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(default=date.today)
    num_stars = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Topping
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Pizza
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name
