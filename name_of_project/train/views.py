from django.shortcuts import render
from  .models import Train
from .models import TrainTicket
from django.shortcuts import get_object_or_404,redirect 
# Create your views here.

#Train List 
def Train_list(request):
    # "-" is for descending order
    trains = Train.objects.all().order_by('Date_of_departure')
    return render (request , "index.html",{'trains':trains})

#booking the thing 
def Booked_Train_ticket(request):
    ticket = get_object_or_404(Train)
    if ticket.seatNo>0:
        ticket.seatNo -=1
        ticket.save()
        return ticket




