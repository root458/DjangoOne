from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.one = '1st-big-item.jpg'
    dest1.img = '1st-item.jpg'
    dest1.price = 200
    dest1.check = True

    dest2 = Destination()
    dest2.name = 'Muhabe'
    dest2.desc = 'Also we never sleep'
    dest2.one = '2nd-big-item.jpg'
    dest2.img = '2nd-item.jpg'
    dest2.price = 150
    dest2.check = False

    dest3 = Destination()
    dest3.name = 'Honshyu'
    dest3.desc = 'Same here'
    dest3.one = '6th-big-item.jpg'
    dest3.img = '6th-item.jpg'
    dest3.price = 180
    dest3.check = True

    dests = [dest1, dest2, dest3]     # PUT THE OBJECTS TO A LIST THEN PASS JUST THE LIST

    return render(request, 'index.html',{'dests':dests})

    # THIS IS HOW TO PASS OBJECTS TO HTML PAGES
