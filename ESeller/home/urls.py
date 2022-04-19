from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home')
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup", views.handleSignup, name="handleSignup"),
    path("login", views.handleLogin, name="handleLogin"),
    path("logout", views.handleLogout, name="handleLogout"),
    path("search", views.search, name='search'),
    path("checkout", views.checkout, name='checkout'),

    #Products
    path("fruit", views.fruit, name='fruit'),
    path("vegetable", views.vegetable, name='vegetable'),
    path("toy", views.toy, name='toy'),
    path("medicine", views.medicine, name='medicine'),
    path("stationery", views.stationery, name='stationery'),
    path("pet", views.pet, name='pet'),
    path("electric", views.electric, name='electric'),
    path("meat", views.meat, name='meat'),
    path("fish", views.fish, name='fish'),

    #Add product
    path("add_product", views.add_product, name='add_product'),

    #Cart and Checkout
    path("cart", views.cart, name='cart'),
    path("checkout", views.checkout, name='checkout'),


    # for delete and Update
    path("delete_product/<int:product_id>", views.delete_product, name='delete_product'),
    path("update_product/<int:product_id>", views.update_product, name='update_product'),

    #for Admin contact
    path("contact_admin",views.contact_admin, name='contact_admin'),
    path("sendEmails_contact_admin/<int:message_id>",views.sendEmails_contact_admin, name='sendEmails_contact_admin'),
    path("deleteEmails_contact_admin/<int:message_id>",views.deleteEmails_contact_admin, name='deleteEmails_contact_admin'),
    path("replies_contact_admin",views.replies_contact_admin, name='replies_contact_admin'),
    path("deleteEmails_Sent_replies_admin/<int:message_id>",views.deleteEmails_Sent_replies_admin, name='deleteEmails_Sent_replies_admin'),





]