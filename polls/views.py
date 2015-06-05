from django.conf import settings
# from django.contrib import message
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import login, authenticate, login as auth_login
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404, render


# Create your views here.

def login(request):
	c= {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def auth_view(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username = username, password = password)
	if user is not None:
		auth_login(request, user)
		return HttpResponseRedirect('/polls/loggedin/')	

		
	else:
		return HttpResponseRedirect('/polls/invalid/')


# def valid(request):
# 	contextdict = {}
# 	if request.user.is_authenticated():
# 		contextdict['username']	= request.user.username
# 	context = RequestContext(request, contextdict)
# 	return render(request, '/auth/', context)		


def loggedin(request):
	return render_to_response('loggedin.html', {'full_name':request.user.username})


def invalid_login(request):
	return render_to_response('invalid_login.html')


def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

	

def request_mail(request):
	d = {}
	d.update(csrf(request))
	return render_to_response('send_mail.html', d)	


def send_mail_info(request):
	subject = request.POST.get('subject', '')
	message = request.POST.get('message', '')
	to_email = request.POST.get('to_email', '')
	from_mail = settings.EMAIL_HOST_USER
	if subject and message and to_email:
		try:
			send_mail(subject, message, from_mail, [to_email])	
		except BadHeaderError:
			return HttpResponse('invalid Header found')
		return HttpResponseRedirect('/polls/loggedin/')
	else:
		return HttpResponse('make sure all fields are filled')



def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})



