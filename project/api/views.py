from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Question.objects.all()
    # シリアライザーを取得
    serializer_class = QuestionSerializer

class JobGroupingList(APIView):

    def get(self, request):
        # return HttpResponse("aaaa")
        return Response(
            {
                "paidPublication": 'test',
                "freePublication": 'test',
            }
        )