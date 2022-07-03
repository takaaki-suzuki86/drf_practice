from django.http import HttpResponse
from rest_framework import viewsets
# from .models import Question
from ..models import Question
from .serializer import QuestionSerializer


# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Question.objects.all()
    # シリアライザーを取得
    serializer_class = QuestionSerializer


# class TestViewSet(APIView):
#     queryset = ''
#     http_method_names = ["get"]  # これでGETしかできないようになります
#
#     def get(self, request, format=None):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)
#     #
    # def list(self, request):
    #     db1 = Question.objects.all()
    #     # db2 = Question.objects.db_manager("database2").all() # default以外のDB
    #     return Response({"result": "オッケー！"})
