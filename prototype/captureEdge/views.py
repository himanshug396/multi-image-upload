from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from .forms import ImageForm
from django.http import JsonResponse
from django.views import View
import time
from django.contrib import messages
from prototype.settings import MEDIA_ROOT

def homepage(request):
    claims = Claim.objects.all()
    context = { 'claims' : claims }
    if(len(claims) == 0):
    	messages.error(request, f"No Claim Found. Contact Admin.")
    return render(request, 'homepage.html', context)

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
			messages.info(request, f"(+91) {phone} is already associated with the chosen Claim.")
			return redirect('homepage')
		
		image_url = str(claim_id) + '/' + phone + '/'
		#image_url send to the person on his phone
		messages.success(request, f"Link Sent to {name} at (+91) {phone}")
		
	return redirect('homepage')


def upload_form(request, claim_id, phone):
	if request.method == 'POST':
		time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
		form = ImageForm(request.POST or None, request.FILES or None,)
		if form.is_valid():
			for field in request.FILES.keys():
				for formfile in request.FILES.getlist(field):
					claim_obj = Claim.objects.get(pk=claim_id)
					claim_obj.photo_set.create(phone=phone, photo=formfile)
					claim_obj.save()
					data = {'is_valid': True, 'url': '/media/media/claim_id_' + str(claim_id) + '/' + str(formfile.name), 'name': formfile.name}
		else:
			messages.error(request, f"Some Erro Occured. Reload the page.")
			data = {'is_valid': False}
		return JsonResponse(data)
	else:
		if(Phone.objects.filter(claim_id=claim_id, phone=phone).exists()):
			form =  ImageForm()
		else:
			return HttpResponse("404: URL Not Found")
	return render(request, 'upload.html', {'form': form, 'claim_id': claim_id, 'phone': phone})
