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
	request.session['claim_id'] = claim_id
	request.session['phone'] = phone
	# if request.method == 'POST':
	# 	form_create = ImageForm(request.POST or None, request.FILES or None,)
	# 	if form_create.is_valid():
	# 		for field in request.FILES.keys():
	# 			for formfile in request.FILES.getlist(field):
	# 				img = Photo(photo=formfile)
	# 				img.save()
	# 				print(img)
	return render(request, 'captureEdge/upload.html')


def upload_images(request):
	claim_id = request.session['claim_id']
	phone = request.session['phone']
	if request.method == 'POST':
		print(request.FILES.keys())
		for field in request.FILES.keys():
			for formfile in request.FILES.getlist(field):
				img = Photo(claim_id=claim_id, phone=phone, photo=formfile)
				img.save()
				print(img)	
	print(claim_id)
	print(phone)
	
	return HttpResponse("success: ")


# def upload_form(request, claim_id, phone):
# 	ImageFormSet = modelformset_factory(Photo, form=ImageForm, extra=3)
# 	if request.method == 'POST':
# 		formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
# 		if formset.is_valid():
# 			for form in formset.cleaned_data:
# 				image = form['image']
# 				photo = Photo(claim_id=claim_id, phone=phone, photo=image)
# 				photo.save()
# 				# messages.success(request,"Posted!")
# 			return HttpResponseRedirect('captureEdge/upload.html')
# 		else:
# 			print(formset.errors)
# 	else:
# 		formset = ImageFormSet(queryset=Photo.objects.none())
# 	return render(request, 'captureEdge/upload.html', {'formset': formset})