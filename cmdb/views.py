from django.http import HttpResponsePermanentRedirect


def index(request):
	return HttpResponsePermanentRedirect('/admin')
