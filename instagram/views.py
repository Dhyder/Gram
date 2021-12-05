from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from django.views.generic import RedirectView
from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
