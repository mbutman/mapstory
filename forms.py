from django import forms

from account.forms import SignupForm

from mapstory.models import ContactDetail

class ProfileForm(forms.ModelForm):
    
    blurb = forms.CharField(widget=forms.Textarea)
    biography = forms.CharField(widget=forms.Textarea)
    education = forms.CharField(widget=forms.Textarea)
    expertise = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = ContactDetail
        exclude = ('user','fax','delivery','zipcode','area','links')
        

class CheckRegistrationForm(SignupForm):
    '''add a honey pot field and verification of a hidden client generated field'''
    
    not_human = forms.BooleanField(
                widget=forms.HiddenInput,
                required = False)

    def clean(self):
        if not self.data.get('human',None):
            raise forms.ValidationError('If you are human, ensure you say so.')
        return self.cleaned_data

    def clean_not_human(self):
        if self.cleaned_data['not_human']:
            raise forms.ValidationError('')
