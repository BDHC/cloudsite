from django.db import models
import os

# Create your models here.

class FileUpload(models.Model):
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return os.path.split(self.file.name)[1]

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)