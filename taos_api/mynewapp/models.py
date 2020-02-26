from django.db import models

class TestModel(models.Model):
    """A Test Model"""

    name = models.CharField(max_length=256, blank=True, null=True)