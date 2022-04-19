from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header  =  "Welcome to ESeller"  
admin.site.site_title  =  "ESEller"
admin.site.index_title  =  "ESeller Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
