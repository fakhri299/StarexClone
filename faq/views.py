from rest_framework.generics import ListAPIView
from.models import Category,Question
from.serializers import CategorySerializer,QuestionSerializer



class CategoryApi(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer




class QuestionbyategoryApi(ListAPIView):
    serializer_class=QuestionSerializer


    def get_queryset(self):
        category_slug=self.kwargs.get('slug')
        return Question.objects.filter(category__slug=category_slug)


class QuestionApi(ListAPIView):
    queryset=Question.objects.all()[:9]
    serializer_class=QuestionSerializer