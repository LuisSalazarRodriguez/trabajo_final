from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializers import *

class IndexView(APIView):
    
    def get(self,request):
        context = {'ok':True,
                   'message':'el servidor está activo!'
                   }
        return Response(context)
    
class FavoritoView(APIView):
    def get(self,request):
        dataFavorito = Favorito.objects.all()
        serFavorito = FavoritoSerializer(dataFavorito,many=True)
        return Response({'ok':True,
                        'content':serFavorito.data})