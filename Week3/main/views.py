from django.shortcuts import render

# Create your views here.

def todo_list(request):
    todo_list = [
        {'task': 'Task 1', 'created': '01/05/2018', 'due_on': '03/05/2018', 'owner': 'admin', 'mark': 'Done'},
        {'task': 'Task 2', 'created': '02/05/2018', 'due_on': '04/05/2018', 'owner': 'admin', 'mark': 'Done'},
        {'task': 'Task 3', 'created': '03/05/2018', 'due_on': '05/05/2018', 'owner': 'admin', 'mark': 'Done'},
        {'task': 'Task 4', 'created': '04/05/2018', 'due_on': '06/05/2018', 'owner': 'admin', 'mark': 'Done'},        
    ]
    return render(request, 'todo_list.html', {"todo_list": todo_list})

def completed_todo_list(request):
    completed_todo_list = [
        {'task': 'Task 0', 'created': '10/04/2018', 'due_on': '15/04/2018', 'owner': 'admin', 'mark': 'Done'},        
    ]
    return render(request, 'completed_todo_list.html', {"completed_todo_list": completed_todo_list})