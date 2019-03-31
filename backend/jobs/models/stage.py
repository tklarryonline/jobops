from django.db import models
from model_utils.models import TimeStampedModel


class Stage(TimeStampedModel, models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    datetime = models.DateTimeField(verbose_name='when', null=True, blank=True)
    _is_finished = models.BooleanField(default=False)
    contact_person = models.ForeignKey('ContactPerson', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} at {self.job} ({self.is_finished})'

    @property
    def is_finished(self):
        return 'Finished' if self._is_finished else 'Pending'
