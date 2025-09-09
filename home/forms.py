from django import forms
from .models import Feedback, ContactSubmission

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows':4,'placeholder':'write your feedback...'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email']
        message = forms.CharField(widgets=forms.Textarea)

        def clean_message(self):
            message = self.cleaned_data.get("message")
            if len(message.strip()) < 10:
                raise forms.ValidationError("Message must be at least 10 character long")
            return message