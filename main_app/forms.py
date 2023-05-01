from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control",
                                                                        'id': "name",
                                                                        'type': "text",
                                                                        'placeholder': "Your Name *",
                                                                        'data-sb-validations': "required"
                                                                        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control",
                                                           'id': "email",
                                                           'type': "email",
                                                           'placeholder': "Your Email *",
                                                           'data-sb-validations': "required,email"
                                                           }))
    phone = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': "form-control",
                                                                         'id': "phone",
                                                                         'type': "tel",
                                                                         'placeholder': "Your Phone *",
                                                                         'data-sb-validations': "required"
                                                                         }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': "form-control",
                                                                            'id': "message",
                                                                            'placeholder': "Your Message *",
                                                                            'data-sb-validations': "required"
                                                                           }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

