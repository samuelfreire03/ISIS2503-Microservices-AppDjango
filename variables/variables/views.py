from .models import Variable
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
from bson.objectid import ObjectId
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

@api_view(["GET", "POST"])
def VariableList(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    variables = db['variables']
    if request.method == "GET":
        result = []
        data = variables.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                "variable": dto['variable']
            }
            result.append(jsonData)
        client.close()
        context = {
            'variable_list': result
        }
        return render(request, 'Variable/variables.html', context)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = variables.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)

def VariableCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        variable = Variable()
        variable.name = data_json["name"]
        variable.save()
        return HttpResponse("successfully created variable")