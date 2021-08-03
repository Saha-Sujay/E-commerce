from django.core.checks import messages
from django.shortcuts import redirect, render
from django.views import View
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_log ,logout

class ProductView(View):
    def get(self, request):
        topwears= Product.objects.filter(category='TW')
        bottomwears= Product.objects.filter(category='BW')
        mobiles= Product.objects.filter(category='M')
        laptops= Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears , 'mobiles':mobiles, 'laptops':laptops })

class ProductDetailView(View):
    def get(self, request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    mobiles= Product.objects.filter(category='M')
    mob1=mobiles
    if data==None:
        mobiles= Product.objects.filter(category='M')
    else:
        mobiles= Product.objects.filter(category='M').filter(brand= data)
    mm=[]
    for m in mob1:
        if m.brand not in mm:
            mm=mm+[m.brand]
    print(mobiles.count)
    return render(request, 'app/mobile.html',{'mm':mm, 'mobile':mobiles,'mob':mob1})

def login(request):
    if request.method=="POST":
        print("post")
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(request, username=email, password=password)
        if user is not None:
            auth_log(request,user)
            print("logged in")
            return  redirect('/')
        else:
            print("invalid credentials")
            return  render(request,'app/login.html')
    else:
        return  render(request,'app/login.html')
def customerregistration(request):
    if request.method== "POST":
        username=request.POST['username']
        email= request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.Info(request,"Username not available")

            elif User.objects.filter(email=email).exists():
                messages.Info(request,"Email already registered")
                print("Email already registered")
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('/')
        else:
            messages.Info(request,"Password 1 and password 2 should be same")
        return render(request, 'app/customerregistration.html')
    else:
        return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def loggout(request):
    logout(request)
    return redirect('/')