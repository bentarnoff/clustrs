from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from dashboard.models import Clustr, Nugget, UserProfile
from django.core.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from registration.backends.default.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from forms import ContributeForm, ClustrsSearchForm

#single clustr view
def clustr(request, clustr):
	clustr = "&" + clustr
	c = Clustr.objects.get(name=clustr)
	nuggets = c.nugget_set.all()
	return render_to_response("single_clustr.html", {'clustr': clustr, 'nuggets': nuggets})

#user auth
def login(request):
	form = AuthenticationForm()
	return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user:
		if user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/dashboard/hello')
		else:
			return HttpResponse("Sorry, it looks like your Clustrs account was disabled. Drop us a line at hello@clustrs.com and we'll try to figure out what happened.") 
	else:
		return HttpResponseRedirect('/dashboard/invalid')

def invalid_login(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/start/')

#dashboard

@login_required
@ensure_csrf_cookie
def hello(request):
	clustrs = request.user.userprofile.active_clustrs.all()
	return render_to_response('hello.html', {'clustrs': clustrs}, context_instance=RequestContext(request))

@login_required
def my_clustrs(request):
	my_clustrs = request.user.userprofile.active_clustrs.all()
	contribute = ContributeForm(my_clustrs=my_clustrs)
	find = ClustrsSearchForm()
	return render_to_response('my_clustrs.html', {'my_clustrs': my_clustrs, 'find': find}, context_instance=RequestContext(request))

@login_required
def remove(request):
	if request.method == 'POST':
		clustr_to_remove = request.POST.get('clustr', '')
		c = Clustr.objects.get(name = clustr_to_remove)
		u = UserProfile.objects.get(user=request.user)
		c.userprofile_set.remove(u)
		my_clustrs = request.user.userprofile.active_clustrs.all()
		find = ClustrsSearchForm()
		return render_to_response('my_clustrs.html', {'my_clustrs': my_clustrs, 'find': find}, context_instance=RequestContext(request))
	my_clustrs = request.user.userprofile.active_clustrs.all()
	find = ClustrsSearchForm()
	return render_to_response('my_clustrs.html', {'my_clustrs': my_clustrs, 'find': find}, context_instance=RequestContext(request))

@login_required
def add(request):
	if request.method == 'POST':
		clustr_to_add = request.POST.get('clustr_input', '')
		c = Clustr.objects.get(id = clustr_to_add)
		u = UserProfile.objects.get(user=request.user)
		c.userprofile_set.add(u)
		my_clustrs = request.user.userprofile.active_clustrs.all()
		find = ClustrsSearchForm()
		return render_to_response('my_clustrs.html', {'my_clustrs': my_clustrs, 'find': find}, context_instance=RequestContext(request))
	my_clustrs = request.user.userprofile.active_clustrs.all()
	find = ClustrsSearchForm()
	return render_to_response('my_clustrs.html', {'my_clustrs': my_clustrs, 'find': find}, context_instance=RequestContext(request))

@login_required
def my_queue(request):
	my_queue = request.user.userprofile.queue.all()
	return render_to_response('my_queue.html', {'my_queue': my_queue}, context_instance=RequestContext(request))

@login_required
def qremove(request):
	if request.method == 'POST':
		nugget_to_remove = request.POST.get('nugget', '')
		n = Nugget.objects.get(id = nugget_to_remove)
		u = UserProfile.objects.get(user=request.user)
		n.nuggets_in_queue.remove(u)
		#nuggets_in_queue
		my_queue = request.user.userprofile.queue.all()
		return render_to_response('my_queue.html', {'my_queue': my_queue}, context_instance=RequestContext(request))
	my_queue = request.user.userprofile.queue.all()
	return render_to_response('my_queue.html', {'my_queue': my_queue}, context_instance=RequestContext(request))

@ensure_csrf_cookie
@login_required
def qadd(request):
	if request.method == 'POST':
		request.META['CSRF_COOKIE_USED'] = True
		nugget_to_add = request.POST.get('nugget', '')
		n = Nugget.objects.get(id = nugget_to_add)
		u = UserProfile.objects.get(user=request.user)
		n.nuggets_in_queue.add(u)
		clustrs = request.user.userprofile.active_clustrs.all()
		return render_to_response('hello.html', {'clustrs': clustrs}, context_instance=RequestContext(request))
	clustrs = request.user.userprofile.active_clustrs.all()
	return render_to_response('hello.html', {'clustrs': clustrs}, context_instance=RequestContext(request))

#@login_required
#def upvote(request):
#	if request.method == 'POST':
#		nugget_to_upvote = request.POST.get('nugget', '')
#		n = Nugget.objects.get(id = nugget_to_upvote)
#		u = UserProfile.objects.get(user=request.user)
#		n.nuggets_in_queue.remove(u)
#		#nuggets_in_queue
#		my_queue = request.user.userprofile.queue.all()
#		return render_to_response('my_queue.html', {'my_queue': my_queue}, context_instance=RequestContext(request))
#	my_queue = request.user.userprofile.queue.all()
#	return render_to_response('my_queue.html', {'my_queue': my_queue}, context_instance=RequestContext(request))

def signup_success(request):
	return render_to_response('signup_success.html')