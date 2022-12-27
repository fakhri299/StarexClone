from rest_framework.generics import ListAPIView
from .models import Shop,Country
from.serializers import ShopSerilizer,CountrySerializer
from rest_framework.permissions import AllowAny


class ShopListApiView(ListAPIView):
    queryset=Shop.objects.all()
    serializer_class=ShopSerilizer
    permission_classes=[AllowAny]



class ShopByCategoryApiView(ListAPIView):
    serializer_class=ShopSerilizer


    def get_queryset(self):
        country_slug=self.kwargs.get('slug')
        return Shop.objects.filter(country__slug=country_slug)


class CountryApi(ListAPIView):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()