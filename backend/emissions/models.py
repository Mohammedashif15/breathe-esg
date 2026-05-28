from django.db import models


class EmissionRecord(models.Model):

    SCOPE_CHOICES = [
        ('SCOPE_1', 'Scope 1'),
        ('SCOPE_2', 'Scope 2'),
        ('SCOPE_3', 'Scope 3'),
    ]

    REVIEW_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    source_type = models.CharField(
        max_length=50
    )

    activity_type = models.CharField(
        max_length=100
    )

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    quantity = models.FloatField()

    unit = models.CharField(
        max_length=50
    )

    normalized_unit = models.CharField(
        max_length=50
    )

    emission_factor = models.FloatField(
        default=0.5
    )

    co2e = models.FloatField()

    is_suspicious = models.BooleanField(
        default=False
    )

    review_status = models.CharField(
        max_length=20,
        choices=REVIEW_CHOICES,
        default='PENDING'
    )

    locked_for_audit = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.activity_type} - {self.co2e}"