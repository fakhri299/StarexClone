from .models import Question,Category
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'