from rest_framework import serializers
from main.models import Task, TodoList
from users.serializers import UserSerializer


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id', 'title',)


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    group = TodoListSerializer()

    class Meta:
        model = Task
        fields = ('id', 'owner', 'group', 'title', 'status')


class TaskSerializerRetrieveRequest(serializers.ModelSerializer):
    owner = UserSerializer()
    group = TodoListSerializer()

    class Meta:
        model = Task
        fields = ('id', 'owner', 'group', 'title', 'created_at', 'due_date', 'status')
