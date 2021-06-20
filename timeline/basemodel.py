from django.db import models
from PIL import Image


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, image, *args, **kwargs):
        """
        Fixes profile photo sizes to 400px * 400px
        """
        super().save(*args, **kwargs)
        if image:
            img = Image.open(image.path)
            if img.height > 400 or img.width > 400:
                output_size = (400, 400)
                img.thumbnail(output_size)
                img.save(image.path)
