# Generated by Django 2.1.7 on 2019-03-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_contactperson_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactperson',
            options={'verbose_name_plural': 'contact people'},
        ),
        migrations.AlterField(
            model_name='stage',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='when'),
        ),
    ]
