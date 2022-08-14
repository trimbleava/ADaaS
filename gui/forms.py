from django import forms
from django.core.mail import send_mail, BadHeaderError

# Create your forms here.

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length = 50)
    contact_email = forms.EmailField(required=True, max_length = 50)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        max_length = 2000
    )

    def __init__(self, *args, **kwargs):
        print("init...................")
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Content:"

        """_summary_
            def send_email(self):
        # send email using the self.cleaned_data dictionary
        print("send_email")
        try:
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data.get('email', 'noreply@mysite.com')
             # ['email@mysite.com'] 
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
        

    def clean(self):
        This is where you should be checking for required
        fields and making sure the submitted data is safe.
        print("clean..............")
        pass
        """
