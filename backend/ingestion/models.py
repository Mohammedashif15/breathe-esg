from django.db import models


class DataSource(models.Model):

    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    uploaded_file = models.FileField(
        upload_to='uploads/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.source_type} - {self.id}"


class RawRecord(models.Model):

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        related_name='raw_records'
    )

    raw_json = models.JSONField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"RawRecord {self.id}"