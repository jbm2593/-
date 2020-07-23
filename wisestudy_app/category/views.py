from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    '''
    카테고리 API
    ---
    111
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    @api_view(['GET'])
    def list(self, request, *args, **kwargs):
        '''
        카테고리 목록 조회 API
        ---
        사용가능한 카테고리 목록을 조회합니다.
        '''

        return super().list(request, args, kwargs)

# @csrf_exempt
# def getAllOrCreateCategory(request):
#     if request.method == 'GET':
#         query_set = Category.objects.all()
#         print(query_set)
#         serializer = CategorySerializer(query_set, many = True)
#         return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CategorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
# #단건조회
# @csrf_exempt
# def getCategory(request, id):
#
#     category = Category.objects.get(category_id=id)
#
#     if request.method == 'GET':
#         serialized_data = CategorySerializer(category)
#         return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer_data = CategorySerializer(category,data=data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return JsonResponse(serializer_data.data, status=201)
#         return JsonResponse(serializer_data.errors, status=400)
#
#     elif request.method == 'DELETE':
#         category.delete()
#         return HttpResponse(status=204)
