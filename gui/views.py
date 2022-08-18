from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.edit import FormView

from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'gui_home.html'
    print("views.homeviews........................")

    def get_context_data(self, **kwargs):
        print("gui.HomeView - get_context_data ...................")
        print(kwargs)
        context = super(HomeView, self).get_context_data(**kwargs)
        print(context)
        context['message'] = 'Hello World!'  # in gui_home.html -- <p>{{ message }}</p> {{variable}} {% tag %}
        return context


class ContactView(FormView):
    template_name = 'gui_contact.html'
    form_class = ContactForm
    success_url = '/success'   # defined in urls

    print("views.contactview.................")
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        print("views.form_valid..................")
        
         # django.core.mail.send_mail is a light wrappers over_Python mail sending interface via the smtplib module.
        # mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT settings. 
        # the EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings, if set, are used to authenticate to the SMTP server, 
        # and the EMAIL_USE_TLS and EMAIL_USE_SSL settings control whether a secure connection is used.
        #
        # send_mail(subject, message, from_email, recipient_list, fail_silently=False, 
        #           auth_user=None, auth_password=None, connection=None, html_message=None)
        #
        # send email using the self.cleaned_data dictionary. 
        # clean method protects against header injection by forbidding newlines in header values
 
        print("forms.send_email....................")
        try:
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            recipient_list = ['beheenmt@gmail.com']
            if form.cleaned_data['cc_myself']:
                recipient_list.append(from_email)
            # send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
        return super(ContactView, self).form_valid(form)


class SuccessView(TemplateView):
    print("views.success...................")
    template_name = "gui_success.html"
    

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
	return render(request, "gui_contact.html", {'form':form})



