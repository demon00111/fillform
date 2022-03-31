from django.core import validators
from django.shortcuts import render,redirect
from .models import user

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def formss(request):
   

    if request.method =='POST':

        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        fm = user(username=user_name,password=user_password,cpassword=confirm_password,email=email) 
        fm.save()
    else:
        fm = user()
    
    
    return render(request,'home.html')

    
#this is for show submited data
def sub(request):
    st = user.objects.all()
    return render(request,'submit.html',{'submit':st})
    

def delete_data(request,pk):   
        user.objects.filter(id=pk).delete()
        return redirect('submit')
    

def edit_data(request , id):
    
    data= user.objects.get(pk=id)

    if request.method =='POST':
        

        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        data.username = user_name
        data.password = user_password
        data.cpassword = confirm_password
        data.email = email
        data.save()

        return redirect('submit')
    else:
        return render(request,'upgrade.html',{"data":data}) 