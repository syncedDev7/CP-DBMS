from django.shortcuts import render
from  .models import Train
from .models import TrainTicket
from django.shortcuts import get_object_or_404,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import UserRegistrationForm
# Create your views here.


#Train List 
def Train_list(request):
    # "-" is for descending order
    trains = Train.objects.all()
    return render (request , "index.html",{'trains':trains})

#booking the thing 
# @login_required
def Booked_Train_ticket(request,train_id):
    ticket = get_object_or_404(Train, id = train_id)
    if ticket.seatNo>0:
        ticket.seatNo -=1
        ticket.save()
        
        return render (request, 'ticket.html',{'ticket':ticket})
    return redirect('train_list')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('train_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})


