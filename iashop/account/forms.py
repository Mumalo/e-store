from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth.models import User
# from crispy_forms.layout import Layout, Fieldset, Row
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout
# from crispy_forms.helper import FormHelper
from django.utils.translation import ugettext_lazy as _
from material import Layout, Row, Fieldset




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
        self.layout = Layout(
                    Fieldset('Account Info',
                        'username', 'email',
                             Row('password', 'password2')),

                    Fieldset('Pesonal details',
                             Row('first_name', 'last_name'),
                             )
        )






    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'password')





class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.layout = Layout(
           Fieldset('Fill The form to Log in',
                    'username',
                    'password')
        )


        super(LoginForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):



     def __init__(self, *args, **kwargs):
        self.layout = Layout(
           Fieldset('',
                    'institution',
                    'gender',
                    'agree_to_terms'),
        )
        super(ProfileForm, self).__init__(*args, **kwargs)

     def clean_agree_to_terms(self):

         if self.cleaned_data.get('agree_to_terms') is False:
             raise ValidationError('Click to agree to terms and conditions')





     class Meta:
         model = Profile
         fields = ('institution', 'gender','agree_to_terms')







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

    def clean_new_password(self):
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
        self.layout = Layout(
            Row('photo','cover'),
            'phone',
            'institution',
            'gender',
            'bio',
        )
        super(ProfileEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('photo','cover', 'phone', 'institution', 'gender', 'bio')




