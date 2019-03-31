from django.db import models
from model_utils.models import TimeStampedModel


class Job(TimeStampedModel, models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=255)
    contacts = models.ManyToManyField('ContactPerson', related_name='jobs')

    def __str__(self):
        return f'{self.title} @ {self.company}'
