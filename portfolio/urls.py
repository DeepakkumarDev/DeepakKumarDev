from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('resource/',views.Resource,name='resource'),
    path('contact/success/', views.contact_success_view, name='contact_success'),


]