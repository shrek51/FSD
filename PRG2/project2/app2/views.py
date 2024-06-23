from django.shortcuts import render
from datetime import timedelta
import datetime
from django.http import HttpResponse
# Create your views here.
def offsetCurrentDateTime(request):
    now = datetime.datetime.now()
    ahead_time = now + timedelta(hours=4)
    behind_time = now - timedelta(hours=4)
    resp1 = "<h2>Current Date and Time is %s</h2>"%(now)
    resp2 = "<h2>Date and Time 4 hours ahead will be %s</h2>"%(ahead_time)
    resp3 = "<h2>Date and Time 4 hours before was %s</h2>"%(behind_time)
    resp = resp1 + resp2 + resp3
    return HttpResponse(resp)