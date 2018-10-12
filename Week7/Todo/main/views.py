from django.shortcuts import render, redirect
from .models import Todo
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def todo_list(request):
    if request.method == "GET":
        todo_list = Todo.objects.filter(mark=False)
    return render(request, 'todo_list.html', {"todo_list": todo_list})

def completed_todo_list(request):
    if request.method == "GET":
        completed_todo_list = Todo.objects.filter(mark=True)
    return render(request, 'completed_todo_list.html', {"completed_todo_list": completed_todo_list})

def todo_add(request):
    if (request.method == 'POST'):
        task = request.POST['task']
        created = datetime.datetime.now()
        due_on = request.POST['due_on']
        owner = request.POST['owner']
        mark = False
        todo = Todo(task = task, created = created, due_on = due_on, owner = owner, mark = mark)
        todo.save()
        return redirect('/todos')
    return render(request, 'todo_add.html')

@csrf_exempt
def todo_delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    if(request.method == 'POST'):
        # todo.delete()
        todo.mark = True
        todo.save()
        return redirect('/todos')
    return render(request, 'todo_delete.html', {"todo": todo})

def delete_complete_list(request):
    todos = Todo.objects.filter(mark=False)
    todos.delete()
    return render(request, 'todo_list.html', {"todo": todos})

def delete_incomplete_list(request):
    todos = Todo.objects.filter(mark=True)
    todos.delete()
    return render(request, 'todo_list.html', {"todo": todos})