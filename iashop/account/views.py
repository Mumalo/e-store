from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .forms import ProfileForm, LoginForm, UserForm, PasswordChangeForm, UserEditForm, ProfileEditForm
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Follow
from notifications.signals import notify
# from notify.signals import notify
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
                    return redirect(user_detail, pk=user.id)
                else:
                    HttpResponse('User currently Inactive')
            else:
                messages.error(request, 'Invalid User')
    else:
        form = LoginForm()
    return render(request,
                  'account/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'home.html')



def user_registration(request):

    if request.method == 'POST':
        user = UserForm(request.POST)
        profile = ProfileForm(request.POST)

        if user.is_valid() and profile.is_valid():
            new_user = user.save()
            new_user.set_password(user.cleaned_data['password'])
            new_user.save()
            users = User.objects.exclude(id=new_user.id)
            users = list(users)
            notify.send(new_user, recipient=users, verb='created a new account')

            return redirect(user_login)
        else:
            HttpResponse('Invalid form')
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
def edit_profile(request, pk):
    user = get_object_or_404(User,  pk=pk)

    if request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserEditForm(instance=user,
                            data=request.POST)

            profile_form = ProfileEditForm(instance=user.profile,
                                  data=request.POST,
                                  files=request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, "Your account was updated successfully")

        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
        return render(
            request, 'account/edit.html',
            {'user_form':user_form,
            'profile_form':profile_form,
             'user':user}
        )
    else:
        raise PermissionDenied







@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    nfs = user.notifications.unread()

    if user.is_authenticated and user.is_active:
        return render(request, 'account/user_home.html', {
        'user': user, 'nfs':nfs
    })

    else:
        raise PermissionDenied


# AJAX view to follow and unfollow users


@ajax_required
@login_required
@require_POST
def user_follow(request):
    # user_id = request.POST.get('id')
    # action = request.POST.get('action')
    # some = {'yeah': 'me'}

    # if user_id and action:
    #     try:
    #         user = User.objects.get(id=user_id)
    #
    #         if action == 'follow':
    #             Follow.objects.get_or_create(
    #                 user_followed=user,
    #                 user_following=request.user
    #             )
    #
    #         else:
    #             Follow.objects.filter(
    #                 user_followed=user,
    #                 user_following=request.user
    #             ).delete()
    #         return JsonResponse({'status': 'ok'})
    #     except user.DoesNotExist:
    #         return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})








# Create your views here.
