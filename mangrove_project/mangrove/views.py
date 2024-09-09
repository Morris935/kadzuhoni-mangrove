from django.shortcuts import render


# mangrove/views.py
def home(request):
    return render(request, 'mangrove/home_page.html')

def about(request):
    return render(request, 'mangrove/about.html')

def contact(request):
    return render(request, 'mangrove/contact.html')

def volunteer(request):
    return render(request, 'mangrove/volunteer.html')

def donate(request):
    return render(request, 'mangrove/donate.html')

def partner(request):
    return render(request, 'mangrove/partner.html')

def impact(request):
    return render(request, 'mangrove/impact.html')

def reforestation(request):
    return render(request, 'mangrove/reforestation.html')

def education(request):
    return render(request, 'mangrove/education.html')

def research(request):
    return render(request, 'mangrove/research.html')

def policy(request):
    return render(request, 'mangrove/policy.html')

def products(request):
    return render(request, 'mangrove/products.html')

def ecotourism(request):
    return render(request, 'mangrove/ecotourism.html')