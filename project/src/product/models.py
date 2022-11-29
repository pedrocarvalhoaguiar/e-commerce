from django.db import models
from src.utility.models import BaseModel
from field_history.tracker import FieldHistoryTracker

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=5000, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=999999.99)

    field_history = FieldHistoryTracker(['price'])

    def __str__(self):
        return self.name