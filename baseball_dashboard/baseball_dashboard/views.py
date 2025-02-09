from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Batting
from .serializers import BattingSerializer

@csrf_exempt
def batting(request):

    if request.method == 'GET':
        bats = Batting.objects.filter(playerid="uriasju01", yearid="2018").get()
        serializer = BattingSerializer(bats)
        return JsonResponse(serializer.data, safe=False)