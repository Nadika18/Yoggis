
from django.shortcuts import render
from django.http.response import StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse

# import view sets from the REST framework
from rest_framework import viewsets
from django.conf import settings
# import the TodoSerializer from the serializer file
from .serializers import YogaSerializer
 
# import the Todo model from the models file
from .models import Yoga,YogaScore

if settings.SERVE:
    from .posedetection import gen_frames

# create a class for the Todo model viewsets
class YogaView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = YogaSerializer
 
    # define a variable and populate it
    # with the Todo list objects
    queryset = Yoga.objects.all()

#put below code in a class to render somewhere
def videofeed(request):
    if settings.SERVE:
        response= StreamingHttpResponse(gen_frames(), content_type="multipart/x-mixed-replace; boundary=frame")
        response['Cache-Control'] = 'no-cache'
        return response
    return HttpResponseRedirect(reverse('home'))

def yoga(request):
    return render(request, 'yoggis/yoga.html')

def home(request):
    trending_yogas = Yoga.objects.all()
    if len(trending_yogas) >= 4:
        trending_yogas = trending_yogas[0:4]
    leaderboard = YogaScore.objects.all()
    if len(leaderboard) >= 5:
        leaderboard = leaderboard[0:5]
    context = {
        "trending_yogas" : trending_yogas,
        "leaderboard" : leaderboard
    }
    return render(request, 'yoggis/home.html', context)

def general(request):
    yogas= Yoga.objects.all()
    general_yogas=yogas.filter(yoga_category__type__contains="General")
    general=general_yogas.filter(difficulty__contains="C")
    context={
        "general":general
    }
    return render(request, 'yoggis/general.html',context)
def chronic(request):
    yogas= Yoga.objects.all()
    asthma=yogas.filter(yoga_category__type__contains="Asthma")


    context={
        "asthma":asthma
    }
    return render(request, 'yoggis/chronic.html',context)
    
def challenges(request):
    return render(request,'yoggis/challenges.html')
def squad(request):
    return render(request,'yoggis/squad.html')

def session(request):
    return render(request,'yoggis/session.html')
def chronic(request):
    return render(request,'yoggis/chronic.html')

def tpose(request):
    return render(request,'yoggis/tpose.html')
# def leaderboard(request):
#     return render(request,'yoggis/leaderboard.html')
