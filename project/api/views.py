from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

