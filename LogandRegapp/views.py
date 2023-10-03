from django.shortcuts import render
from django.views import View
from .models import Register
from django.http import HttpResponse

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,'home.html')
class Regin(View):
    def get(self,request):
        return render(request,'register.html')
class Registerview(View):
    def post(self,request):
        if request.method == 'POST':
            Fname = request.POST['f1']
            Lname = request.POST['f2']
            FLname = request.POST['f3']
            Address = request.POST['f4']
            Email = request.POST['f5']
            password = request.POST['f6']
            re_password = request.POST['f7']
            Mobile = int(request.POST['f8'])
            #print(Fname,Lname,FLname,Address,Email,password,re_password,Mobile)
            data = Register(Fname=Fname, Lname=Lname, FLname=FLname, Address=Address,
                            Email=Email, password=password, re_password=re_password, Mobile=Mobile)
            data.save()
            return HttpResponse("Registration successful!")
            #return render(request,'register.html')

class Valid(View):
    def post(self,request):
        email = request.POST['t1']
        password = request.POST['t2']
        res = Register.objects.filter(Email=email,password=password)
        print(email,password)
        if res:
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Login failed!")





