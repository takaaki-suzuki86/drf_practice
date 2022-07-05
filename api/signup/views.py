import logging

from rest_framework import viewsets
from ..models import Question
from .serializer import QuestionSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Question.objects.all()
    # シリアライザーを取得
    serializer_class = QuestionSerializer

