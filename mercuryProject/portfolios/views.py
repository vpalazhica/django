from django.shortcuts import render
from .models import Portfolios
# Create your views here.
def home(request):
    portfolios = Portfolios.objects
    return render(request, 'home.html', {'portfolios': portfolios})
