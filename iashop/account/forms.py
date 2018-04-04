from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from material import Layout, Row, Fieldset
from .models import Profile, State, City, Lga
import requests
import json


def get_all_cities():

    try:
        cities = requests.get("http://locationsng-api.herokuapp.com/api/v1/cities")
        cities_status_code = cities.status_code

        if cities_status_code == 200:
            print("the response")
            cities = json.loads(cities.content.decode('utf-8'))
            return cities
            print("Request for getting all cities successful")
    except:
        print("There was an issue while attempting to get all cities")


def get_lgas_and_states():

    try:
        lgas = requests.get("http://locationsng-api.herokuapp.com/api/v1/lgas")
        lgas_status_code = lgas.status_code

        if lgas_status_code == 200:
            lgas = json.loads(lgas.content.decode('utf-8'))
            return lgas
            print("Request for getting all lgas successful")
    except:
        print("There was an issue while attempting to get all lgas")


def load_states_info():
    print(State.objects.count())
    if State.objects.count() < 36:
        states = get_lgas_and_states()
        if states:
            for state in states:
                name = state['state']
                lgas = state['lgas']
                print("saving state {} into the db".format(name))
                current_state = State.objects.create(name=name)
                current_state.state_loaded = True
                current_state.save()
                for lga in lgas:
                    print("saving lga ==> {} belonging to state {}".format(lga, name))
                    current_lga = Lga.objects.create(state=current_state, name=lga)
                    current_lga.lga_loaded = True
                    current_lga.save()
        else:
            print("action==>attempted to load request data onto the db")
            print("failure==>the request returned nothing")
    else:
        print("All 36 states have already been loaded  into the database")

print(load_states_info())


class UserForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput,)

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data['password']
        password2 = cleaned_data['password2']

        if password1 in self.cleaned_data:
            if (password1 != password2):
                raise forms.ValidationError("Passwords don\'t match")
            elif (len(password1) < 5) or (len(password2) < 5):
                raise forms.ValidationError("Password must be greater than 5 characters")
        return password2

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'Repeat Password'
        self.fields['password'].widget.attrs.update({'class': 'input','id': 'pass'})
        self.fields['password2'].widget.attrs.update({'class': 'input','id': 'pass'})
        self.fields['username'].widget.attrs.update({'class': 'input','id': 'user'})
        self.fields['email'].widget.attrs.update({'class': 'input','id': 'email'})


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input',})



class ProfileForm(ModelForm):

     def __init__(self, *args, **kwargs):

        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['state'].widget.attrs.update({'class': 'input','id': 'user'})
        self.fields['state'].required = False
        self.fields['lga'].required = False
        self.fields['lga'].widget.attrs.update({'class': 'input'})
        self.fields['gender'].required = False
        self.fields['bio'].required = False
        self.fields['phone'].required = False
        self.fields['agree_to_terms'].label = 'I agree to the terms and conditions'

     def clean_agree_to_terms(self):
         if self.cleaned_data.get('agree_to_terms') is False:
             raise ValidationError('Click to agree to terms and conditions')
         return self.cleaned_data.get('agree_to_terms')

     class Meta:
         model = Profile
         fields = ('state', 'gender', 'agree_to_terms', 'bio', 'phone', 'lga')



class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    retype_password = forms.CharField(max_length=25, widget=forms.PasswordInput)

    def __init__(self, data=None, user=None, *args, **kwargs):

        self.user = user
        super(PasswordChangeForm, self).__init__(data=data, *args, **kwargs)

    def clean_current_password(self):
        cleaned_data = self.cleaned_data

        current_password = cleaned_data['current_password']

        existing_password = self.user.check_password('current_password')

        if not existing_password:
            raise ValidationError('Wrong password!')

        return cleaned_data

        cleaned_data = self.cleaned_data
        new_password = cleaned_data['new_password']
        retyped_password = cleaned_data['retype_password']

        if (len(new_password == 0) or len(retyped_password == 0)):
            raise ValidationError("Password cannot be left blank")

        if (new_password != retyped_password):
            raise ValidationError("Passwords must be equal!!")

        return cleaned_data

    def save(self):
        self.user.set_password(self.new_password)
        return self.user

class UserEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.layout = Layout(
            Row('first_name', 'last_name'),
            'email',
        )
        super(UserEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['lga'].widget.attrs.update({'class': 'input'})

    class Meta:
        model = Profile
        fields = ('photo', 'phone', 'state', 'gender', 'bio', 'lga')




