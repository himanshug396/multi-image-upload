from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


def homepage(request):
    claims = Claim.objects.all()
    context = { 'claims' : claims }
    return render(request, 'captureEdge/homepage.html', context)

def user_details(request):
	if request.method == 'POST':
		claim_id = int(request.POST.get('claim_id'))
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		
		claim_obj = Claim.objects.get(pk=claim_id)
		claim_obj.name = name
		claim_obj.phone = phone
		claim_obj.save()
		
		image_url = str(claim_id) + '/' + phone + '/'
	
		#image_url send to the person on his phone
	return HttpResponse("success: " + image_url)
