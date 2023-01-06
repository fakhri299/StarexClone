from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from.serializers import *

class CountryDetailApi(RetrieveAPIView):
    serializer_class=CountryDetailSerializer
    queryset=Country.objects.all()
    lookup_field='slug'



class CountryListApi(ListAPIView):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()
    


class ProfileDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()




    
        








    



