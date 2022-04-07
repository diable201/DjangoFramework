from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Task
from main.serializers import TaskSerializerRetrieveRequest, TaskSerializer


class TodoListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('group_id') is not None:
            return Task.objects.filter(group_id=self.kwargs.get('group_id'))
        return Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskSerializerRetrieveRequest
        return TaskSerializer


class TodoRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('group_id') is not None:
            return Task.objects.filter(group_id=self.kwargs.get('group_id'))

    def get_serializer_class(self):
        if self.action == 'completed':
            return TaskSerializerRetrieveRequest

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(
            tasks.filter(
                group_id=self.kwargs.get('group_id'),
                status=Task.DONE
            ),
            many=True,
            data=self.request.data
        )
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
