
from distutils.log import error
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404


from calc.models import Marks

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    user_id=request.POST['username']
    # marks=Marks()
    # mark=Marks.objects.get(id=user_id)
    # if (marks):
    #     return render(request,'result.html',{'marks':mark})
    # else:
    #     return render(request,'failed.html')
    try:
        mark = Marks.objects.get(id=user_id)
        return render(request,'result.html',{'marks':mark})
    except Marks.DoesNotExist:
            return render(request,'failed.html')
   


