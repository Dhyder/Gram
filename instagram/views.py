from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
