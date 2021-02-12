from django.shortcuts import redirect, render



# Create your views here.
from .forms import RegisterationForm
from .models import RegisteredUser
def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('formSuccess/')
    else:
        form = RegisterationForm()
    return render(request, 'registration.html', {'form': form})

def form_successfull(request):
    return render(request,'succussfull.html')

# def viewRegisteredUser(request,mail):
#     reg_user = RegisteredUser.objects.get(email_address_excat=mail)
#     return render(request, 'registration.html', {'user':reg_user})