# hotel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donate/', views.donate, name='donate'),
    path('partner/', views.partner, name='partner'),
    path('impact/', views.impact, name='impact'),
    path('reforestation/', views.reforestation, name='reforestation'),
    path('education/', views.education, name='education'),
    path('research/', views.research, name='research'),
    path('policy/', views.policy, name='policy'),
    path('products/', views.products, name='products'),
    path('ecotourism/', views.ecotourism, name='ecotourism'),
]
