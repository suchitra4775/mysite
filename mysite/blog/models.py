from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=25)
    date = models.IntegerField(
        validators = [MinValueValidator(1),MaxValueValidator(5)]
    )
    author = models.CharField(max_length=25)
    slug = models.BooleanField()


    def __str__(self):
        return self.title
