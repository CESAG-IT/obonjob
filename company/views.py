from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    return HttpResponse("Bienvenue sur notre Site Web")

def listCompanyView(request):
    return HttpResponse("Voici la liste des entreprises")

def createCompanyView(request):
    return HttpResponse("Création d'une nouvelle entreprise")

def showCompanyView(request, id):
    return HttpResponse(f"Voici l'entreprise ID : {id}")

def updateCompanyView(request, id):
    return HttpResponse(f"modification de l'entreprise ID : {id}")

def deleteCompanyView(request, id):
    return HttpResponse(f"suppression de  l'entreprise ID : {id}")
