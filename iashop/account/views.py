from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .forms import ProfileForm, LoginForm, UserForm, PasswordChangeForm, UserEditForm, ProfileEditForm
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Profile
from django.contrib.auth.models import User

def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(username=username,
                                     password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(user_home, pk=user.id)
                else:
                    HttpResponse('User currently Inactive')
            else:
                return HttpResponse('Invalid User')
    else:
        form = LoginForm()
    return render(request,
                  'account/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'home.html')


@login_required
def user_registration(request):

    if request.method == 'POST':
        user = UserForm(request.POST)
        profile = ProfileForm(request.POST)

        if user.is_valid() and profile.is_valid():
            new_user = user.save(commit=False)
            new_user.set_password(user.cleaned_data['password'])
            new_user.save()
            new_profile = profile.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return redirect(user_login)
    else:
        user = UserForm()
        profile = ProfileForm()

    return render(request, 'account/registration.html', {'user': user, 'profile': profile})

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)

        if form.is_valid():
            return redirect()
    else:
        form = PasswordChangeForm()
    return render(request, 'account/change_password')

@login_required
def edit_profile(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                            data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile_user,
                                  data=request.POST,
                                  files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile_user)
    return render(
        request, 'account/edit.html',
        {'user_form':user_form,
         'profile_form':profile_form}
    )








def user_home(request, pk):
    user = get_object_or_404(User, pk=pk)

    if user.is_authenticated and request.user.id == user.id:
        return render(request, 'account/user_home.html', {
        'user': user
    })

    else:
        raise PermissionDenied










# Create your views here.
