from django.db import models


# Create your models here.
class Reminders(models.Model):
    REMINDER_METHODS = [("SMS", "SMS"), ("EMAIL", "Email")]
    date = models.DateField()
    time = models.TimeField()
    method = models.CharField(max_length=10, choices=REMINDER_METHODS)
    message = models.TextField()


def __str__(self):
    return f"{self.method} - {self.message[:20]}"
