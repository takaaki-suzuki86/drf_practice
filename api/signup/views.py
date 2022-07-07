import logging

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Question
from .serializer import QuestionSerializer

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Question.objects.all()
    # シリアライザーを取得
    serializer_class = QuestionSerializer


class LineUsersView(APIView):
    # parser_classes = [FormParser, MultiPartParser]
    parser_classes = [JSONParser]

    def get(self, request):
        logger = logging.getLogger(__name__)
        logger.info(__name__)
        logger.info("Hello world!")
        return Response(
            {
                "totalCount": "aaa",
            }
        )

    def post(self, request):
        return Response(
            {
                "totalCount": "aaa",
            }
        )
