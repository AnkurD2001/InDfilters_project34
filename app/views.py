from django.shortcuts import render

# Create your views here.

import datetime

def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Hello every One','dt':dt,'c':1}

    return render(request,'filters.html',d)