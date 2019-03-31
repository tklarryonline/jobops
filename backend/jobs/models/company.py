from django.db import models
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel, models.Model):
    RECRUITMENT_AGENCY = 'RA'
    OUTSOURCING_FIRM = 'OF'
    PROPRIETARY_COMPANY = 'PTY'
    COMPANY_TYPE_CHOICES = (
        ('', 'N/A'),
        (RECRUITMENT_AGENCY, 'Recruitment Agency / Head-hunter'),
        (OUTSOURCING_FIRM, 'Outsourcing Firm / Consultant'),
        (PROPRIETARY_COMPANY, 'Proprietary / Product Software')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=COMPANY_TYPE_CHOICES, blank=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
