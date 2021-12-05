from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from django.views.generic import RedirectView
from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from rest_framework import authentication, permissions

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
