from django.shortcuts import render, redirect
import random
from datetime import datetime

# Location Map for coin min/max
locations = {
    "farm" : (10,20),
    "cave" : (5,10),
    "house" : (1,5),
    "casino" : (0,50)
}

def index(request):
    #If the keys "gold" or "activites" don't already exist in the session dictionary, create them
    if not "gold" in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['count'] = 0
    return render(request, "index.html")

def reset(request):
    #Clear session dictionary and refresh page
    request.session.clear()
    return redirect('/')

def process_money(request, location_name):
    location = locations[location_name]
    #Generate random number between the two numbers referenced in the "locations" dict based on location_name
    current_gold = random.randint(location[0], location[1])
    current_time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    message = f"Earned {current_gold} gold from the {location_name}! ({current_time})"
    result = "win"
    request.session['count'] += 1
    #If casino is selcted, there's a 50% chance the number stored in "current_gold" will become negative
    if location_name == 'casino':
        if random.randint(0,1) > 0:
            message = f"Lost {current_gold} gold from the casino... ouch ({current_time})"
            current_gold = current_gold * -1
            result = "lost"
    request.session['gold'] += current_gold
    request.session['activities'].append({"message": message, "result": result})
    #Player loses if Gold exceeds 100
    if request.session['gold'] > 100:
        request.session['activities'].append({"message": "You lose :(", "result" : "lost"})
    #Player Wins if Gold equals 100
    if request.session['gold'] == 100:
        request.session['activities'].append({"message": "Wow! Incredible!!", "result" : result})
    #Player loses if count reaches 10 before Gold equals 100
    if request.session['count'] == 10 and request.session['gold'] < 100:
            request.session['activities'].append({"message": "You lose :(", "result" : "lost"})
    return redirect("/")