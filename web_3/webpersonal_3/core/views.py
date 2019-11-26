from django.shortcuts import render

# Create your views here.

# crear home abaut porfolio y contact.

def home(request):
    return render(request, "core/home.html" )

def about(request):
    return render(request, "core/about.html" )

def contact(request):
    return render(request, "core/contact.html" )