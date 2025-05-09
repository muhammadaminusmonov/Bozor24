from category.models import Category  
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from ..permissions import IsSeller, IsOwnerOrReadOnly, IsPlatformAdmin
from rest_framework import permissions


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_ctg_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        print(result.data)
        return Response({"data": result.data})
    

@api_view(['GET', 'POST'])
@permission_classes([IsPlatformAdmin])
def admin_ctg_post(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        print(result.data)
        return Response({"data": result.data})
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({'data': 'success'}, status=status.HTTP_201_CREATED)


@api_view(["GET","PUT", "DELETE"])
@permission_classes([IsPlatformAdmin])
def detail_ctg(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Could not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data = request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data)
        
        elif request.method == "PUT":
            serializer = CategorySerializer(category, data=request.data)
            print(serializer.is_valid(), serializer)
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(({"error:Could not edit"}), status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
