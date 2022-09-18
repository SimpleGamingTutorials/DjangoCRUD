from django.db import models

# GOLD = Completed
# SILVER = Midway
# BRONZE  = Starting


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
