from django.shortcuts import render, get_object_or_404
from .models import Conf_hall
from .forms import conf_hallForm
from django.http import HttpResponseRedirect

def conf_hall_list(request):
	
	conf_hall = None
	conf_halls = Conf_hall.objects.all()
	return render(request, 'validator/conf_hall/list.html', {'conf_hall': conf_hall, 'conf_halls': conf_halls})

def conf_hall_detail(request, id):

	conf_hall = get_object_or_404(Conf_hall, id=id)
	return render(request, 'validator/conf_hall/detail.html', {'conf_hall': conf_hall})

#def get_name(request):
#	# if this is a POST request we need to process the form data
#	if request.method == 'POST':
#		# create a form instance and populate it with data from the request:
#		form = conf_hallForm(request.POST)
#		# check whether it's valid:
#		if form.is_valid():
#
#			name = form.cleaned_data["name"]
#
#			second_name = form.cleaned_data["second_name"]
#
#
#			#new_testobject = form.save(commit=True)
#
#			new_testobject = conf_hall(name = name, second_name = second_name)
#
#			new_testobject.save()
#
#
#			# process the data in form.cleaned_data as required
#			# ...
#			# redirect to a new URL:
#			return HttpResponseRedirect('/')
#
#	# if a GET (or any other method) we'll create a blank form
#	else:
#		form = conf_hallForm()
#
#	return render(request, 'validator/conf_hall/name.html', {'form': form})







def add(request):

	form = conf_hallForm()

	if request.method == 'POST':
		form = conf_hallForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'validator/conf_hall/add.html', context)















