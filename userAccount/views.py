from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User,Group
from .models import Customer,Order
# Create your views here.

def logout_page(request):
    logout(request)
    return redirect('/')

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return render(request,"userAccount/login_page.html",{"error_message":"Invalid username or password."})
    else:
        return render(request,"userAccount/login_page.html")
    

def register_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=username).exists():
                error_message = "Username already taken."
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=f_name, last_name=l_name)
                customer_group = Group.objects.get(name='Customer')
                user.groups.add(customer_group)
                user.save()
                c = Customer(user=user)
                c.save()
                login(request,user)
                return redirect(reverse_lazy('home'))
        else:
            error_message = "Passwords do not match."
        context={
            "username":username,
            "f_name":f_name,
            "l_name":l_name,
            "email":email,
            'error_message':error_message
        }
        return render(request,"userAccount/register_page.html",context)
    else:
        return render(request,"userAccount/register_page.html")
    

def profile_page(request):
    user = request.user
    if Customer.objects.filter(user=user).exists():
        customer = user.customer
        orders= Order.objects.filter(customer=customer)
        cart=customer.cart_items.all()
        return render(request,'userAccount/profile.html',{'cart':cart,"orders":orders})
    else:
        return redirect(reverse_lazy('make_customer'))
    
def make_customer(request):
    if request.method=="POST":
        address = request.POST.get('address').lower()
        city = request.POST.get('city').lower()
        state = request.POST.get('state').lower()
        mobile = request.POST.get('mobile')
        c = Customer.objects.get(user=request.user)
        c.address=address
        c.city=city
        c.state=state
        c.mobile=mobile
        c.save()
        return redirect(reverse_lazy('profile'))

    return render(request,'userAccount/make_customer.html')