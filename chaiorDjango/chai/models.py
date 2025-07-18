from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarites(models.Model):
    CHAI_TYPE_CHOICES = (
        ('DP', 'Doodhpati Chai'),
        ('G', 'Ghor Chai'),
        ('KI', 'Kashmiri Chai'),
        ('NR', 'Normal Chai'),
        ('SL', 'Sulemani Chai'),
    )

    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='chais/')
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    
    def __str__(self):
        return self.name
    
