from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for a month",
    "february": " Walk 20 minutes every day",
    "march": "Play table tennis now!",
    "april": "Eat no meat for a month",
    "may": " Walk 20 minutes every day",
    "june": "Play table tennis now!",
    "jule": "Eat no meat for a month",
    "august": " Walk 20 minutes every day",
    "september": "Play table tennis now!",
    "october": "Eat no meat for a month",
    "november": " Walk 20 minutes every day",
    "december": "Play table tennis now!"
}

def index(request):
    months = list(monthly_challenges.keys())
 
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_as_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month.")

    desired_month = months[month-1]
    desired_path = reverse("month-challenge", args = [desired_month])
    return HttpResponseRedirect(desired_path) 

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        
    except:
        return HttpResponseNotFound("This page is not supported!")
    
