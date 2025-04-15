from django.shortcuts import render
from portfolio.models import PortfolioInfo


# Create your views here.
def home(request):
    portfolio_info = PortfolioInfo.objects.first()
    return render(request, "core/home.html", {"portfolio_info": portfolio_info})


def about(request):
    return render(request, "core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    return render(request, "core/contact.html")
