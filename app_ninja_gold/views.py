from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    #Check to see if counter is in session.  If not, set counter to 0 and activies to an array. 
    if 'counter' not in request.session or 'activities' not in request.session: 
        request.session['counter']= 0
        request.session['activities']= []
    return render(request,"index.html")

#Create routing rules for route "/process_money" to process POST method.
def gold(request):
    #If hidden input equals "farm", generate random integer between 10-20.
    if request.POST['property'] == 'farm':
        gold = random.randint(10,20)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + ' ' +  '(' + str(strftime("%Y %m %d %I:%M %p", gmtime())) + ')')
    #If hidden input equals "cave", generate random integer between 5-10.
    elif request.POST['property'] == 'cave':
        gold = random.randint(5,10)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + ' ' +  '(' + str(strftime("%Y %m %d %I:%M %p", gmtime())) + ')')
    #If hidden input equals "house", generate random integer between 2-5.
    elif request.POST['property'] == 'house':
        gold = random.randint(2,5)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + ' ' +  '(' + str(strftime("%Y %m %d %I:%M %p", gmtime())) + ')')
    #If hidden input equals "casino", generate random integer between -50-50.
    elif request.POST['property'] == 'casino':
        gold = random.randint(-50,50)
        #If random integer is less than or equal to 0, have activities display gold lost in red.
        if gold <= 0: 
            request.session['activities'].append('Entered a casino and lost' + ' ' + str(gold) + ' ' + 'golds...' + ' ' + 'Ouch.' + ' ' +  '(' + str(strftime("%Y %m %d %I:%M %p", gmtime())) + ')')
        #If random integer is greater than 0, have activities display amount of gold won in green.
        else:
            request.session['activities'].append('Entered a casino and won' + ' ' + str(gold) + ' ' + 'golds...' + ' ' + 'HUZZAH!' + ' ' +  '(' + str(strftime("%Y %m %d %I:%M %p", gmtime())) + ')')
    request.session['counter'] += gold
    return redirect("/")

#Have the route /reset clear session.
def reset(request):
    del request.session['counter']
    del request.session['activities']
    return redirect("/")
