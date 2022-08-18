from django import forms
from django.template.defaultfilters import mark_safe


# Create your forms here.

class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length = 150, widget=forms.TextInput(attrs={'size': '37'}))
    contact_name = forms.CharField(required=True, max_length = 50)
    from_email = forms.EmailField(required=True, max_length = 50)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=2000, initial="Enter your message here")
    cc_myself = forms.BooleanField(required=False)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # examples
        # self.fields['subject'].widget = forms.widgets.TextInput(
        #    attrs={
        #        'placeholder': 'subject',
        #        'class': 'form-control',
        #        'style': 'padding-left: 5px, margin-left: 10px !important;'
        #    }
        #)
        ###
        # my_field = forms.CharField(
        #                max_length=100,
        #                label = mark_safe('<strong>My Bold Field Label</strong>')
        #            )
        self.fields['subject'].label      = mark_safe('<strong>S u b j e c t</strong>')
        self.fields['contact_name'].label = "Your name:"
        self.fields['from_email'].label   = "Your email:"
        self.fields['message'].label = ""
        self.fields['cc_myself'].label = "Cc myself"
