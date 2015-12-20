from django.shortcuts import render, render_to_response, redirect
from dashboard.models import Clustr, Nugget

def start(request):
	if request.user.is_authenticated():
		return redirect('/dashboard/hello')
	clustrs = Clustr.objects.order_by('id')[:9]
	return render_to_response("start.html", {'clustrs': clustrs})