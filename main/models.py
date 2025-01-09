from django.db import models
from core.models import BaseModel  # Import the BaseModel
from helpers import generate_unique_slug

class Task(BaseModel):  # Inherit from BaseModel
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=256)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
       
        if not self.slug or self.title != Task.objects.filter(pk=self.pk).first().title:
            self.slug = generate_unique_slug(self, 'title', self.title)
        super().save(*args, **kwargs)
