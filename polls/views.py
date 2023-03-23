from django.http import HttpResponse

from django.template import loader

def index(request):
    name = 'HUFS'
    temp = loader.get_template('hello_world.html')
    context = {
        'name' : name,
    }
    return HttpResponse(temp.render(context, request))

def if_else(request):
    warr = True
    vara = 8
    varb = 5
    temp = loader.get_template('hello_if.html')
    context1 = {
        'warranty' : warr,
        'vara' : vara,
        'varb' : varb,
        }
    return HttpResponse(temp.render(context1, request))

import datetime

def for_loop(request):
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.datetime.today().weekday()
    #today = datetime.datetime(2018, 3, 26)
    #today = today.weekday()
    temp = loader.get_template('hello_for.html')
    context = {
        'today' : today,
        'weekday' : weekday,
        }
    return HttpResponse(temp.render(context, request))

def ifequal_func(request):
    vara = 6
    varb = 5
    temp = loader.get_template('hello_ifequal.html')
    context1 = {
        'vara' : vara,
        'varb' : varb,
        }
    return HttpResponse(temp.render(context1, request))