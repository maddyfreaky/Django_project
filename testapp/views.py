from django.shortcuts import redirect, render
from django.http import JsonResponse, Http404
from django.http import HttpResponse
from .models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

def newuser(request):
    return render(request,'newuser.html')

def insertuser(request):
    vuid = request.POST['tuid'];
    vuname = request.POST['tuname'];
    vuemail = request.POST['tuemail'];
    vurole = request.POST['turole'];
    us=User(uid=vuid, uname=vuname, uemail=vuemail, urole=vurole);
    us.save();
    return redirect('/testapp/viewusers')

def viewusers(request):
    user = User.objects.all()
    return render(request,'viewusers.html',{'userdata':user})


def get_user_details(request, user_id):
    try:
        user = User.objects.get(uid=user_id)
        user_data = {
            'uid': user.uid,
            'uname': user.uname,
            'uemail': user.uemail,
            'urole': user.urole
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    



