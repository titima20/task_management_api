from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority']
    ordering_fields = ['due_date', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return TaskUpdateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response({"message": "Task deleted successfully."})

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = not task.completed
        task.status = 'COMPLETED' if task.completed else 'PENDING'
        task.completed_at = timezone.now() if task.completed else None
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
