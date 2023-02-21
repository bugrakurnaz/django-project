from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text  = "Eat no meat for a month"
    elif month == "february":
        challenge_text = " Walk 20 minutes every day"
    elif month == "march":
        challenge_text = "Play table tennis now!"
    else:
        return HttpResponseNotFound("This page is not supported!")
    return HttpResponse(challenge_text)
