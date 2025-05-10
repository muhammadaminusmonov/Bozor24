from comment.models import Comment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .serializers import CommentSerializer
from api.permissions import IsOwnerOrReadOnly, IsPlatformAdmin, IsSeller

class CommentView(APIView):
    parser_classes = [IsSeller, IsPlatformAdmin, IsOwnerOrReadOnly]

    def get(self, request):
        comments = Comment.objects.all()
        result = CommentSerializer(comments, many=True)
        return Response({"data": result.data})

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({"data": CommentSerializer(result).data}, status=status.HTTP_201_CREATED)


class CommentDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly, IsPlatformAdmin, IsSeller]

    def get(self, request, pk):
        try:
            comments = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"Eror":"Could not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            comments = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"Eror":"Could not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"Error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response({"message": "Comment successfully deleted"}, status=status.HTTP_204_NO_CONTENT)