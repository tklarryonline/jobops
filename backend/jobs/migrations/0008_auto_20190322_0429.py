# Generated by Django 2.1.7 on 2019-03-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20190322_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.CharField(blank=True, choices=[('', 'N/A'), ('RA', 'Recruitment Agency / Head-hunter'), ('OF', 'Outsourcing Firm / Consultant'), ('PTY', 'Proprietary / Product Software')], max_length=5),
        ),
        migrations.AddField(
            model_name='job',
            name='contacts',
            field=models.ManyToManyField(related_name='jobs', to='jobs.ContactPerson'),
        ),
    ]
