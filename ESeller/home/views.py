from pydoc import describe
from unicodedata import category
import django
from django.shortcuts import render,HttpResponse,redirect
from markupsafe import re
from datetime import datetime

from matplotlib import image
from home.models import Contact, Product, Sent_replies
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
import os
from django.core.mail import send_mail

from django.db import models
# Create your views here.



def index(request):

    context = {
        "var" : "45265"
    }

    return render(request,'index.html',context)
    #return HttpResponse("Hi, How u doin?")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')




# Client Contact
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        if name!="":
            contact = Contact(name=name,email=email,phone=phone,comment=comment,date=datetime.today())
            contact.save()
            messages.success(request, 'Your response has been submitted successfully!!!')
    return render(request,'contact.html')



# Admin Contact view
@login_required(login_url='/login')
def contact_admin(request):
    if request.user.is_superuser :
      contact = Contact.objects.all().filter(is_replied=False).order_by('-date')
      n = Contact.objects.count()
      params = {'contact': contact, 'n':1}
      return render(request,'contact_admin.html',params)

    else:
        return render(request,'html_view_with_error',{"error" : "PERMISSION DENIED"})





# Admin Send Email Through Contact
def sendEmails_contact_admin(request,message_id):
    if request.method=='POST':
        recipient = request.POST.get('recipient_name')
        subject = request.POST.get('email_subject')
        message = request.POST.get('message_text')

        send_mail(
            subject,
            message,
            'eseller.sunjare@gmail.com',
            [recipient],
            fail_silently=False
        )

        contact = Contact.objects.get(pk=message_id)
        contact.is_replied = True
        contact.save()

        Sent_replies.objects.create(message_sender=contact)
        Sent_replies_message_id = Sent_replies.objects.get(message_sender__message_id=message_id)
        Sent_replies_message_id.reply = message
        Sent_replies_message_id.subject = subject
        Sent_replies_message_id.save()


        messages.success(request, 'Message has been sent successfully!!!')
        return redirect("contact_admin")





# Admin Delete Email Through Contact
def deleteEmails_contact_admin(request,message_id):
        message = Contact.objects.get(pk=message_id)
        message.delete()
        return redirect("contact_admin")





# View Sent Replies
@login_required(login_url='/login')
def replies_contact_admin(request):
    if request.user.is_superuser :
        sent_replies = Sent_replies.objects.all()
        params = {'sent_replies': sent_replies}
        return render(request,'replies_contact_admin.html',params)

# Admin Delete Email Through Sent Replies
def deleteEmails_Sent_replies_admin(request,message_id):
        message = Sent_replies.objects.get(message_sender__message_id=message_id)
        message.delete()
        return redirect("replies_contact_admin")





def search(request):
    return HttpResponse("sfsbs")



def checkout(request):
    return HttpResponse("sdvsdvs")









#For Poducts
def fruit(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Fruit").count()
    params = {'product': product, 'range':range(1,n), 'n':n}
    return render(request,'fruit.html',params)


def vegetable(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Vegetable").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'vegetable.html',params)


def toy(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Toy").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'toy.html',params)


def medicine(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Medicine").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'medicine.html',params)


def stationery(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Stationery").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'stationery.html',params)


def pet(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Pet").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'pet.html',params)


def electric(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Electric").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'electric.html',params)


def meat(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Meat").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'meat.html',params)


def fish(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Fish").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'fish.html',params)








#Cart
def cart(request):
    return render(request,'cart.html')

#Checkout
def checkout(request):
    return render(request,'checkout.html')


#Add Product

def add_product(request):
    if request.method=='POST':

        product_name = request.POST['product_name']
        product_category = request.POST['product_category']
        product_price = request.POST['product_price']
        product_photo = request.FILES['product_photo']
        product_description = request.POST['product_description']
    
        add_product = Product(product_name=product_name,category=product_category,price=product_price,description=product_description, pub_date=datetime.today(),image=product_photo)
        add_product.save()

        messages.success(request, 'Product has been added successfully!!!')
        return render(request,'index.html')    

    else:
        return HttpResponse("404-Not Found") 




# For Deleting Product
def delete_product(request,product_id):
    product = Product.objects.get(pk=product_id)
    os.remove(product.image.path)
    product.delete()
    messages.success(request, 'Product has been deleted successfully!!!')
    return redirect("/")

# For Updating Product
def update_product(request,product_id):

    if request.method=='POST':
            product = Product.objects.get(pk=product_id)
            os.remove(product.image.path)
            product.product_name = request.POST['product_name']
            product.category = request.POST['product_category']
            product.price = request.POST['product_price']
            product.image = request.FILES['product_photo']
            product.description = request.POST['product_description']
            product.pub_date = datetime.today()
            product.save()

            messages.success(request, 'Product has been updated successfully!!!')
            return redirect("/") 
    else:
        return HttpResponse("404-Not Found") 

    








#Handeling Signup + Login + Logout
def handleSignup(request):

    if request.method == 'POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if User.objects.filter(username=username).count()==1:
            messages.warning(request, "This username already exists, Please Choose another!!!")
            return redirect('home')


        if len(username)>10:
            messages.warning(request, " Your username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created successfully!!!")
        return redirect('home')

    else:
        return HttpResponse("404-Not Found")   







def handleLogin(request):

    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In!!!")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials, Please try again :(")
            return redirect('home')

    else:
        return HttpResponse("404-Not Found") 






def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Loggged Out")
    return redirect('home')
