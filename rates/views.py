from rest_framework.generics import ListAPIView
from.serializers import *
from rest_framework.permissions import AllowAny



class RateApi(ListAPIView):
    serializer_class=CountrySerializer

    def get_queryset(self):
        slug=self.kwargs.get('country_slug')
        return Country.objects.filter(slug=slug)


       
