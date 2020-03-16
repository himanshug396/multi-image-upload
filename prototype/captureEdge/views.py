from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'captureEdge/homepage.html')

def phone(request, name, phone, claim_id):
    response = "%s %s %s"
    return HttpResponse(response % phone % name % claimID)

