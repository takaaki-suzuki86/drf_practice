from rest_framework import serializers
from engage.polls.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'id')
        read_only_fields = ('id',)
