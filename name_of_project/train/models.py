from django.db import models

# Create your models here.
from django.db import models 
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
 
class Train(models.Model):
    # dont use max length in integer use validator for it 
    seatNo =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    train_number = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(9999999)])
    from_station = models.TextField(max_length=100)
    to_station = models.TextField(max_length=100)
    Date_of_departure = models.DateField()
    # printed_at = models.DateTimeField(auto_now_add=True) # for initia creation 


class TrainTicket(models.Model): 
    #we will see about this user shit 
    # user = models.ForeignKey(User , on_delete=models.CASCADE, null = True, blank=True)
    
    most_word = models.ForeignKey(Train, on_delete=models.CASCADE)
    Booked_Date = models.DateTimeField(auto_now_add=True)
