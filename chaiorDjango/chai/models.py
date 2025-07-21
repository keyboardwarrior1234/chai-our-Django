from django.db import models
from django.contrib.auth.models import User
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
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    
    def __str__(self):
        return self.name
    

# one to many

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarites, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments =models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    

# many to many 

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    chai_varities = models.ManyToManyField(ChaiVarites,related_name='stores')
    
    def __str__(self):
        return self.name
    
    
 # one to one 
 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarites,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'certificate for {self.name.chai}'
    
    
