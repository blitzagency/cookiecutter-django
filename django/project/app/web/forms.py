from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your name here"
            }
        )
    )

    email = forms.CharField(
        required=True,
        label="E-mail:",
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@yoursite.com"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="E-mail:",
        max_length=255,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Type your message",
                "rows": 4
            }
        )
    )
