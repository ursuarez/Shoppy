from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
	# return HttpResponse('HELLO WORLD')
	return render(request, 'index.html')