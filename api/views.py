from .serialaizes import TaskSerializes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task


@api_view(['GET'])
def my_api_view(request):
    data = {
        'text': 'Hello world !'
    }
    return Response(data)


@api_view(['GET'])
def tasklist_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializes(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail_list_view(request, id):
    detail_list = Task.objects.get(id=id)
    serializer = TaskSerializes(detail_list, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    serializer = TaskSerializes.get(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"Created": "Object is created"})


@api_view(['POST'])
def task_update_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializes(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete_view(request, id):
    task = Task.objects.get(id=id)

    task.delete()
    return Response({"obj": "Delete"})
