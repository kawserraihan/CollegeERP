from django.shortcuts import render
from info.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



# -----------------Index-----------------


@login_required
def index(request):
    if request.user.is_superuser:
        return render(request, 'index.html')
    elif hasattr(request.user, 'teacher'):
        return render(request, 'index.html')
    else:
        message = "You do not have any access"
    
    response_data = {'message': message}
    return JsonResponse(response_data)
        


#-----------------Login USER handling-----------------   



def login_view(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user.is_superuser or hasattr(user, 'teacher'):
            return render(request, 'index.html')
        else:
            context = {'username_incorrect': True}
            return render(request, 'authentication/login.html', context)
        
    return render(request, 'authentication/login.html')



#-----------------Department List-----------------


@login_required
def DepartmentList(request):
    departmentlist = Department.objects.all()

    context = {
        'departments': departmentlist
    }
        
    return render(request, 'coredata/departmentlist.html', context)




#-----------------Runs Only Once In A New Database When There Is No Day To Create Days-----------------
#-----------------Specially Used For Buses-----------------



@login_required
def initialize_days_of_week(request):
    # Check if the days of the week have already been added
    if BusDay.objects.count() == 0:
        days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for day in days_of_week:
            BusDay.objects.create(day=day)
        message = "Days of the week have been added to the BusDay model."
    else:
        message = "Days of the week have already been added to the BusDay model."

    response_data = {'message': message}
    return JsonResponse(response_data)
