from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):

    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', 'A user with that email already exists.')
        return cleaned_data


class UserCompletionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super(UserCompletionForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class ProfileCompletionForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('birth_date', 'mobile_number', 'country', 'state', 'about')
        widgets = {
            'birth_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
    def __init__(self, *args, **kwargs):
        super(ProfileCompletionForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].required = True
        self.fields['mobile_number'].required = True
        self.fields['country'].required = True
        self.fields['state'].required = True
        self.fields['about'].required = True


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', 'A user with that email already exists.')
        return cleaned_data


class ProfileForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ('birth_date', 'mobile_number', 'phone_number',
                  'country', 'state', 'zip_code', 'city', 'district', 'about')
        widgets = {
            'birth_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }


class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password',)
