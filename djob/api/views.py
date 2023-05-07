from rest_framework import generics, status
from rest_framework.response import Response

from ..models import job, Worker, Category
from .serializers import JobPostSerializer, JobGetSerializer, WorkerGetSerializer, WorkerPostSerializer, \
    CategorySerializer
from .permissions import IsAdminAuthorUserOrReadOnly, IsOwnerOrReadOnly


class CategoryCreateApiView(generics.ListCreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer


class CategoryRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class JobCreateApiView(generics.ListCreateAPIView):
    queryset = job
    serializer_class = JobGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JobGetSerializer
        if self.request.method == 'POST':
            return JobPostSerializer
        return Response({'detail': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class JobRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = job
    serializer_class = JobGetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JobGetSerializer
        return JobPostSerializer


class WorkerCreateApiView(generics.ListCreateAPIView):
    queryset = Worker
    serializer_class = WorkerGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkerGetSerializer
        if self.request.method == 'POST':
            return WorkerPostSerializer
        return Response({'detail': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class WorkerRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker
    serializer_class = WorkerGetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkerGetSerializer
        return WorkerPostSerializer


