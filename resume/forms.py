from django import forms

from resume.models import Contact


class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(max_length=32, required=True)
    contact_email = forms.EmailField(required=True)
    contact_content = forms.Textarea()

    # An inline class to provide additional information on the form.
    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_email', 'contact_content')
