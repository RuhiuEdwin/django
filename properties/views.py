import json
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PropertiesSerializer
from .models import Properties
from .models import MultipleImage
# from firebase import serviceAccount
# import pyrebase

# config = {
#     "apiKey": "AIzaSyBkyU4JLMWC3zrAD3ll-kkXDd3msoqjqdM",
#     "authDomain": "urbanridge-88599.firebaseapp.com",
#     "projectId": "urbanridge-88599",
#     "storageBucket": "urbanridge-88599.appspot.com",
#     "messagingSenderId": "563735364688",
#     "appId": "1:563735364688:web:1b3928f363656e57d8fd55",
#     "measurementId": "G-VJ88J4W36D",
#     "serviceAccount": "serviceAccount.json",
#     "databaseURL" : "https://urbanridge-88599-default-rtdb.firebaseio.com"
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()
# storage.child().out()

# Create your views here.

class PropertiesView(viewsets.ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Properties.objects.all()

def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImage.objects.create(images=image)
    images = MultipleImage.objects.all()
    return render(request, 'index.html', {'images': images})