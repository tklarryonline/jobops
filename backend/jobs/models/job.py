from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} @ {self.company}'
