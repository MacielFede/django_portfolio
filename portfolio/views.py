from django.shortcuts import render
from portfolio.models import PortfolioInfo, Project


# Create your views here.
def home(request):
    portfolio_info = PortfolioInfo.objects.first()
    return render(request, "home.html", {"portfolio_info": portfolio_info})


def about(request):
    portfolio_info = PortfolioInfo.objects.first()
    return render(request, "about.html", {"portfolio_info": portfolio_info})


def portfolio(request):
    portfolio_info = PortfolioInfo.objects.first()
    projects = Project.objects.get_queryset()
    return render(
        request,
        "portfolio.html",
        {"portfolio_info": portfolio_info, "projects": projects},
    )


def contact(request):
    portfolio_info = PortfolioInfo.objects.first()
    return render(request, "contact.html", {"portfolio_info": portfolio_info})
