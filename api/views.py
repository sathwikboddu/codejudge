# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Users
import json
from django.core import serializers


# Create your views here.
@csrf_exempt
def leads(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        first_name = data["first_name"]
        last_name = data["last_name"]
        mobile = data["mobile"]
        email = data["email"]
        location_type = data["location_type"]
        location_string = data["location_string"]
        user = Users(first_name=first_name,last_name=last_name,mobile=mobile,email=email,
                     location_type=location_type,location_string=location_string)
        user.save()
        check(mobile)
        return JsonResponse({'first_name':first_name,'last_name':last_name,'mobile':mobile,
                             'email':email,'location_type':location_type,'location_string':location_string,
                             'status':'Created'},status=201)

    elif HttpResponse.status_code == 400:
        return JsonResponse({"status": "failure","reason": "Bad Request"})

    if request.method == 'GET':
        id = request.GET.get('id')
        result = Users.objects.get(pk=id)
        data = serializers.serialize('json', [result,])
        final_result = json.loads(data)
        final_result = final_result[0]['fields']
        final_result['status'] = 'Created'
        # print(final_result)
        return JsonResponse(final_result)
   
    elif HttpResponse.status_code == 400:
        return JsonResponse({"status": "failure","reason": "Bad Request"})
    
    elif HttpResponse.status_code == 404:
        return JsonResponse({})
    
    if request.method == 'PUT':
        id = request.GET.get('id')
        data = json.loads(request.body.decode('utf-8'))
        first_name = data["first_name"]
        last_name = data["last_name"]
        mobile = data["mobile"]
        email = data["email"]
        location_type = data["location_type"]
        location_string = data["location_string"]
        Users.objects.filter(pk=id).update(first_name=first_name,last_name=last_name,
                                           mobile=mobile,email=email,location_type=location_type,
                                           location_string=location_string)
        return JsonResponse({'status':'success'}, status=202)
    
    elif HttpResponse.status_code == 400:
        return JsonResponse({"status": "failure","reason": "Bad Request"})

    if request.method == 'DELETE':
        id = request.GET.get('id')
        Users.objects.filter(id=id).delete()
        return JsonResponse({'status':'success'}, status=200)

    elif HttpResponse.status_code == 400:
        return JsonResponse({"status": "failure","reason": "Bad Request"})

def check(mobile):
    if Users.objects.latest('mobile'):
        return JsonResponse({'status':'success'}, status=200)        

# def fetch(request):
#     if request.method == 'GET':
#         id = request.GET.get('id')
#         result = Users.objects.get(pk=id)
#         data = serializers.serialize('json', [result,])
#         final_result = json.loads(data)
#         final_result = final_result[0]['fields']
#         final_result['status'] = 'Created'
#         print(final_result)
#         return JsonResponse(final_result)
   
#     elif HttpResponse.status_code == 400:
#         return JsonResponse({"status": "failure","reason": "Bad Request"})
    
#     elif HttpResponse.status_code == 404:
#         return JsonResponse({})



# @csrf_exempt
# def update(request):
#     if request.method == 'PUT':
#         id = request.GET.get('id')
#         data = json.loads(request.body.decode('utf-8'))
#         first_name = data["first_name"]
#         last_name = data["last_name"]
#         mobile = data["mobile"]
#         email = data["email"]
#         location_type = data["location_type"]
#         location_string = data["location_string"]
#         Users.objects.filter(pk=id).update(first_name=first_name,last_name=last_name,
#                                            mobile=mobile,email=email,location_type=location_type,
#                                            location_string=location_string)
#         return JsonResponse({'status':'success'}, status=202)
    
#     elif HttpResponse.status_code == 400:
#         return JsonResponse({"status": "failure","reason": "Bad Request"})

# @csrf_exempt
# def delete(request):
#     if request.method == 'DELETE':
#         id = request.GET.get('id')
#         Users.objects.filter(id=id).delete()
#         return JsonResponse({'status':'success'}, status=200)

#     elif HttpResponse.status_code == 400:
#         return JsonResponse({"status": "failure","reason": "Bad Request"})


@csrf_exempt
def mark_lead(request):
    if request.method == 'PUT':
        id = request.GET.get('id')
        data = json.loads(request.body.decode('utf-8'))
        first_name = data["first_name"]
        last_name = data["last_name"]
        mobile = data["mobile"]
        email = data["email"]
        location_type = data["location_type"]
        location_string = data["location_string"]
        communication = data["communication"]
        Users.objects.filter(pk=id).update(first_name=first_name,last_name=last_name,
                                           mobile=mobile,email=email,location_type=location_type,
                                           location_string=location_string,communication=communication)
        return JsonResponse({'status':'success'}, status=202)
    
    elif HttpResponse.status_code == 400:
        return JsonResponse({"status": "failure","reason": "Bad Request"})
