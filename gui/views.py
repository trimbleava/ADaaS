from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import resolve
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.cache import cache

import redis

from gui import forms, models, utils



# Inspecting Redis with the CLI:
# $ redis-cli -n 1
# 127.0.0.1:6379[1]> keys *
# 1) "example:1:views.decorators.cache.cache_header"
# 2) "example:1:views.decorators.cache.cache_page"
# 127.0.0.1:6379[1]> get "example:1:views.decorators.cache.cache_page"
# NOTE: Run the flushall command on the Redis CLI to clear all of the keys from the data store.
#
# decorators = [never_cache, login_required]
# @method_decorator(decorators, name='dispatch')


class HomeView(TemplateView):
    template_name = 'gui_home.html'
    
    def get_context_data(self, **kwargs):
        print("gui.HomeView - get_context_data ...................")
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    """
    This, get, is only called when a form view is loaded for the first time, not when the form is submitted
    Override it when you want to do something before a request is processed by the view, or after
    """
    def get(self, request, *args, **kwargs):
        print("gui.HomeView - get ...................")

        context = self.get_context_data(**kwargs)
        return render(request, 'gui_home.html', context)
        # return super(HomeView, self).get(request, *args, **kwargs)
        #return super(TemplateView, self).render(request,'gui_home.html', context)

    def post(self, request, *args, **kwargs):
        print("gui.HomeView - post ...................")
        
        # name = request.POST.get('predchoice', None)
        # print(name)
        context = self.get_context_data()
        # context.update({"calling_url": request.path})
        # print(context)
        # if context["form"].is_valid():
        #     print('yes done')
            # save your model
            # redirect

        return super(TemplateView, self).render(request,'gui_home.html', context)


    # def dispatch(request, *args, **kwargs) :
    #
    #     # The view part of the view -- the method that accepts a request argument plus arguments, and returns a HTTP response.
    #     # The default implementation will inspect the HTTP method and attempt to delegate to a method that matches the HTTP method;
    #     # a GET will be delegated to get(), a POST to post(), and so on.
    #
    #     # The default implementation also sets request, args and kwargs as instance variables, so any method on the view can know
    #     # the full details of the request that was made to invoke the view.
    #     print("in dispatch")
    #     return request


from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['contact_name'], 
			'email': form.cleaned_data['contact_email'], 
			'message':form.cleaned_data['content'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})



