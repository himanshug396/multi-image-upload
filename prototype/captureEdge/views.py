from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from .forms import ImageForm
from django.http import JsonResponse
from django.views import View
import time

def homepage(request):
    claims = Claim.objects.all()
    context = { 'claims' : claims }
    return render(request, 'captureEdge/homepage.html', context)

def user_details(request):
	if request.method == 'POST':
		claim_id = int(request.POST.get('claim_id'))
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		phone.replace(" ", "")
		claim_obj = Claim.objects.get(pk=claim_id)
		try:
			claim_obj.phone_set.create(name=name,phone = phone)
		except:
			return HttpResponse("Failure: " + "The Phone is already associated with the chosen ClaimID")
		
		image_url = str(claim_id) + '/' + phone + '/'
	
		#image_url send to the person on his phone
	return HttpResponse("success: " + image_url)


def upload_form(request, claim_id, phone):
	if request.method == 'POST':
		time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
		form = ImageForm(request.POST or None, request.FILES or None,)
		if form.is_valid():
			for field in request.FILES.keys():
				for formfile in request.FILES.getlist(field):
					claim_obj = Claim.objects.get(pk=int(claim_id))
					claim_obj.photo_set.create(phone=phone, photo=formfile)
					claim_obj.save()
					data = {'is_valid': True}
		else:
			data = {'is_valid': False}
		return JsonResponse(data)
	else:
		form =  ImageForm()
	return render(request, 'captureEdge/upload.html', {'form': form, 'claim_id': claim_id, 'phone': phone})
