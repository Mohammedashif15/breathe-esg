from django.db import models
from emissions.models import EmissionRecord


class Review(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUSPICIOUS', 'Suspicious'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('LOCKED', 'Locked'),
    ]

    emission = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    analyst_name = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    comments = models.TextField(
        blank=True,
        null=True
    )

    reviewed_at = models.DateTimeField(
        auto_now=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.emission.id} - {self.status}"