from django.forms import forms
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

from django.db.models import Q
from .models import SignUpData, packages, custom


def sample1(request):
    return render(request,"index.html")

def sample2(request):
    return render(request,"destination.html")

def sample3(request):
    return render(request,"travel.html")

def sample4(request):
    return render(request,"login.html")
# Login database

# def signin(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method=="POST":
#             username=request.POST['username']
#             password=request.POST["password"]
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 return redirect('/signin')
#         else:
#             return render(request,"login.html")
#
# fn=''
# un=''
# em=''
# ph=''
# pwd=''
# cp=''
# gen=''

def sample5(request):
    return render(request, 'regester.html')
# global fn,un,em,ph,pwd,cp,gen
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="vivek",database='register')
#         cursor = m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="first_name":
#                 fn=value
#             if key=="user_name":
#                 un=value
#             if key=="email":
#                 em=value
#             if key=="number":
#                 ph=value
#             if key=="password":
#                 pwd=value
#             if key=="confirm_password":
#                 cp=value
#             if key=="gender":
#                 gen=value
#         c="insert into register Values('{}','{}','{}','{}','{}','{}','{}')".format(fn,un,em,ph,pwd,cp,gen)
#         cursor.execute(c)
#         m.commit()

def sample6(request):
    return render(request,"user.html")
def sample7(request):
    return render(request,"contact.html")

def sample8(request):
    return render(request,"about.html")


def SignUpDatafunction(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phonenum = request.POST.get('phonenum', '').strip()
        password = request.POST.get('password', '').strip()

        # Basic data validation
        if not (fullname and username and email and phonenum and password):
            return render(request, 'your_template.html', {'error_message': 'All fields are required'})

        # Validate email format
        if '@' not in email or '.' not in email:
            return render(request, 'your_template.html', {'error_message': 'Invalid email format'})

        # Validate phone number format
        if not phonenum.isdigit() or len(phonenum) != 10:
            return render(request, 'your_template.html', {'error_message': 'Phone number must be a 10-digit number'})

        # Check if email already exists
        if SignUpData.objects.filter(sign_Email=email).exists():
            return render(request, 'your_template.html', {'error_message': 'Email already exists'})

        # Create new SignUpData object and save it
        signobj = SignUpData(sign_FullName=fullname, sign_Username=username, sign_Email=email, sign_PhoneNumber=phonenum, sign_password=password)
        signobj.save()

        # Redirect to login page or do whatever you need to do
        return render(request, "login.html")
    else:
        # Handle GET request here if needed
        return render(request, "your_template.html")
def checkuserlogin(request):
    username=request.POST["username"]
    pwd=request.POST["password"]
    flag=SignUpData.objects.filter(Q(sign_Username=username) & Q(sign_password=pwd))
    if flag:
        user = SignUpData.objects.get(sign_Username=username)
        request.session["uname"] = user.sign_Username
        return render(request, "user.html", {"uname": user.sign_Username})
    else:
        return render(request, "logfail.html")



def payment(request,id):
    r=packages.objects.filter(pid=id)
    return render(request, "payment.html", {"d": r[0]})

def custom(request):
    country = request.POST['country']
    State = request.POST['State']
    city = request.POST['city']
    Hotels = request.POST['Hotels']
    UserRating = request.POST['UserRating']
    PropertyType = request.POST['PropertyType']
    Chains = request.POST['Chains']
    Amenities = request.POST['Amenities']
    obj=custom(country=country,State=State,city=city,Hotels=Hotels,UserRating=UserRating,PropertyType=PropertyType,Chains=Chains,Amenities=Amenities)
    custom.save(obj)
    r=custom.objects.all()
    return render(request, "customhtm.html",{"data":r})


def addcustom(request):
    return render(request, "custom.html")

def sucpayment(request):
    return render(request, "paymsuc.html")


def searchcity(request,city,days,type,n):
    r=packages.objects.filter(name=city)

    p=r[0]

    return render(request, "te.html",{"name":p.name,"imgurl":p.imgurl,"price":p.price*days,"des":p.des,"pid":p.pid})


def sear(request):
    return render(request, "search.html")

def destination(request):
    r=destination.objects.all()
    return render(request, "destination.html",{"data":r})

def feedback(request):
    return render(request,"feedback.html")
