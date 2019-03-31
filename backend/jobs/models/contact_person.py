from django.db import models
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class ContactPerson(TimeStampedModel, models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    position = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'contact people'

    def __str__(self):
        return f'{self.name} @ {self.company}'
