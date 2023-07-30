from django.shortcuts import render, redirect
from home.models import Contact, Home, Base_Details, Home_Slide_Images
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm, HomeRegistration
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from datetime import datetime

# Create your views here.

def home(request):
    form = HomeRegistration()
    return render(request, "index.html", {'form':form})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def loginUser(request):
    return render(request, "login.html")

def RegisterUser(request):
    return render(request, "register.html")

class CustomerRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form':form})


    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Register Successfully!")
            form.save()
        return render(request, 'register.html', {'form':form})


def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/login')


def save_contact(request):
    # if request.is_ajax():
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(name, email, subject, message)
        contact = Contact(name=name, email=email, subject=subject, message=message, date_time=datetime.now())
        # print(contact)
        contact.save()
        stud = Contact.objects.values()
        student_data = list(stud)
        data = {'status':'Save', 'student_data':student_data}
        return JsonResponse(data)
        # return JsonResponse({'name':name, 'email':email, 'subject':subject, 'messege':messege})

@csrf_exempt
def home_save(request):
    if request.method == "POST":
        subscribe = request.POST.get('subscribe')
        home = Home(subscribe=subscribe)
        home.save()
        stud = Home.objects.values()
        student_data = list(stud)
        data = {'status':'Save', 'student_data':student_data}
        return JsonResponse(data)




def page_not_found(request, exception):
    return render(request, "error_404.html", {})