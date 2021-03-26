from django.db import models


# Create your models here.
class ProjectImageUploader(models.Model):
    file = models.FileField(upload_to='ProjectImages', blank=False, null=False)

    def __str__(self):
        return self.file.name

