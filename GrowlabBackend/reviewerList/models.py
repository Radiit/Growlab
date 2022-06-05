from django.db import models

# Create your models here.


class ReviewerList(models.Model):
    name            = models.CharField(max_length=200, blank=False)
    price           = models.CharField(max_length=100, blank=True)
    rating          = models.CharField(max_length=1, blank=True)
    job             = models.TextField(max_length=255, blank=False)

    def __str__(self):
        return self.name
  