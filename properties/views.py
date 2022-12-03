import json
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PropertySerializer
from .models import Property
from .models import PropertyImages
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

class PropertyView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
