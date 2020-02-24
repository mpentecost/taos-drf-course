from django.db import models

from people.models import Person


class Dealership(models.Model):
    """A representation of a Dealership"""
    name = models.CharField(max_length=256)
    max_fleet_count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    general_manager = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="managed_dealerships"
    )
    sales_reps = models.ManyToManyField(Person, related_name="dealerships")

    def __str__(self):
        """A string representation of this model"""
        return f'{self.id}: {self.name}'


class Auto(models.Model):
    """A representation of an Automobile"""
    # Class Choices
    CAR = "car"
    TRUCK = "truck"
    SUV = "suv"

    AUTO_CLASS_CHOICES = (
        (CAR, CAR),
        (TRUCK, TRUCK),
        (SUV, SUV)
    )

    auto_model = models.CharField(max_length=256)
    auto_class = models.CharField(max_length=32, choices=AUTO_CLASS_CHOICES)
    num_doors = models.IntegerField()
    dealer = models.ForeignKey(Dealership, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """The string representation of this model"""
        return f'{self.id}: {self.auto_model}'


class Sale(models.Model):
    """A sale of an auto"""
    date_sold = models.DateTimeField()
    autos = models.ManyToManyField(Auto, related_name='sales')
    sales_rep = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='sales')
    sale_amount = models.IntegerField()

    def __str__(self):
        """The string representation of this model"""
        return f'{self.id}: {self.sale_amount} on {self.date_sold}'
