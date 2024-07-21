from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_home_page(request):
    return HttpResponse(render(request, "home.html"))

def show_contact_us(request):
    return HttpResponse(render(request, "contactus.html"))

def show_about_us(request):
    return HttpResponse(render(request, "aboutus.html"))
