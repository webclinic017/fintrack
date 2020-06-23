from django.db import models
from industry.models import Industry


class Company(models.Model):
    short_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    long_name = models.CharField(max_length=512, unique=True, null=False, blank=False)
    business_summary = models.TextField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry_companies')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = "Companies"
        ordering = ['short_name', ]

    def __str__(self):
        return self.short_name
