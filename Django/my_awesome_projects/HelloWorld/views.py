from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    university_selected="University of Maryland"
    list_of_all=[
            "University of Florida",
            "Arizona State University",
            "Indiana University",
            "Virginia Tech",
            "Colorado Boulder",
    ]
    context={
        "university": university_selected,
        "list":list_of_all,
    }
    response=render(request,'index.html',context)
    return response
    