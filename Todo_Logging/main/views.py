from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Task, TodoList
from main.serializers import TaskSerializerCreateUpdateRequest, TaskSerializer, TodoListSerializer
import logging

logger = logging.getLogger(__name__)


class TodoListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        logger.debug('some debug message')
        logger.info('some info message')
        logger.warning('some warning message')
        logger.error('some error message')
        logger.critical('some critical message')
        if self.kwargs.get('group_id') is not None:
            return TodoList.objects.filter(group_id=self.kwargs.get('group_id'))
        return TodoList.objects.all()

    def get_serializer_class(self):
        logger.debug('some debug message')
        logger.info('some info message')
        logger.warning('some warning message')
        logger.error('some error message')
        logger.critical('some critical message')
        return TodoListSerializer

    @action(methods=['get'], detail=False)
    def todos(self, request, *args, **kwargs):
        logger.debug('some debug message')
        logger.info('some info message')
        logger.warning('some warning message')
        logger.error('some error message')
        logger.critical('some critical message')
        tasks = Task.objects.filter(group_id=self.kwargs.get('group_id'))
        serializer = TaskSerializer(
            tasks,
            many=True
        )
        return Response(serializer.data)


class TodoRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        logger.debug('some debug message')
        logger.info('some info message')
        logger.warning('some warning message')
        logger.error('some error message')
        logger.critical('some critical message')
        if self.kwargs.get('pk') is not None:
            return Task.objects.filter(id=self.kwargs.get('pk'))
        return Task.objects.all()

    def get_serializer_class(self):
        logger.debug('some debug message')
        logger.info('some info message')
        logger.warning('some warning message')
        logger.error('some error message')
        logger.critical('some critical message')
        if self.action == 'create' or self.action == 'update':
            return TaskSerializerCreateUpdateRequest
        return TaskSerializer
