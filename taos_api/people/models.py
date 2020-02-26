from django.db import models


class Person(models.Model):
    """A representation of a Person"""
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """The string representation of this model"""
        return f'{self.id}: {self.last_name}, {self.first_name}'
  
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
