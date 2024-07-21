from django.shortcuts import render
import datetime
from  django.http import HttpResponse
# Create your views here.
def currentDateTime(request):
    now = datetime.datetime.now()
    resp = "<h2>Current Date and Time is %s</h2>"%(now)
    return HttpResponse(resp)

