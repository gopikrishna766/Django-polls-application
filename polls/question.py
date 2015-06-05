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
from django.views import generic
from django.shortcuts import get_object_or_404, render




class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
