from django.db import models
from src.utility.models import BaseModel
from field_history.tracker import FieldHistoryTracker
import uuid
import pathlib
from django.conf.global_settings import MEDIA_ROOT

# Create your models here.
class Product(BaseModel):
    def path_to_image_product(self, filename):
        extension = pathlib.Path(filename).suffix
        new_filename = str(uuid.uuid4()) + extension
        return f'product/images/{new_filename}'

    name = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=5000, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=999999.99)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField('image', null=True, upload_to=path_to_image_product)

    field_history = FieldHistoryTracker(['price'])

    def __str__(self):
        return self.name