from django import forms

class mainForm(forms.Form):
    fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 90, 'rows': 10, 'placeholder': 'Message'}))
