import uuid
from django.db import models
from django.db.models import Max


# Create your models here.
from Category.models import Category


class Project(models.Model):
    Id = models.IntegerField(default=1)
    ProjectId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    CategoryId = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    Name = models.CharField(max_length=1000, null=True, blank=True, default=None)
    Description = models.CharField(max_length=10000, null=True, blank=True, default=None)
    DisplayOrder = models.IntegerField()
    IsActive = models.BooleanField(default=False)

    # Don't Touch it, This Method will Auto Increment Id Field for every new record
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = Project.objects.all().aggregate(Max('Id'))['Id__max']
            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.Id = last_id + 1
        super(Project, self).save(*args, **kwargs)

    # This Method Marks Model Object with a string
    def __str__(self):
        return self.Name


class Image(models.Model):
    Id = models.AutoField(primary_key='True')
    ProjectId = models.ForeignKey(Project, null=True, blank=True, default=None, related_name="Images", on_delete=models.CASCADE)
    FileName = models.CharField(max_length=1000, null=True, blank=True, default=None)

    # This Method Marks Model Object with a string
    def __str__(self):
        return self.FileName

