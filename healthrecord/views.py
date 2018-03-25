from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def summition(request):
    # c=a+b


    return HttpResponse( "kc")
    # return HttpResponse("Your sum is==>" + str(c))

def index(request):
   my_data = request.GET
   a=float(my_data.get('a'))
   b=float(my_data.get('b'))
   c=a+b
   return HttpResponse("Your sum is==>" + str(c))

