from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listJobView(request):
    return HttpResponse("Voici la liste des emplois")

def createJobView(request):
    return HttpResponse("Création d'une nouvelle emploi")

def showJobView(request, id):
    return HttpResponse(f"Voici l'emploi ID : {id}")

def updateJobView(request, id):
    return HttpResponse(f"modification de l'emploi ID : {id}")

def deleteJobView(request, id):
    return HttpResponse(f"suppression de  l'emploi ID : {id}")
