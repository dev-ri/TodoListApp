from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from . models import TodoItem


def todo(request):
    todo_items = TodoItem.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'todo/todo.html',
        {
            'title':'Todo',
            'message':'Your Todo App page.',
            'year':datetime.now().year,
            'todo_items':todo_items,
        }
    )

def addtodo(request):
    if request.method == 'POST':
        todoitem = TodoItem(text = request.POST['text'])
        todoitem.save()
        return HttpResponseRedirect('/todo/')
    else:
        return HttpResponseRedirect('/todo/')

def deletetodo(request, item_id):
    if request.method == 'POST':
        item_to_dlt = TodoItem.objects.get(id = item_id)
        item_to_dlt.delete()
        return HttpResponseRedirect('/todo/')
    else:
        return HttpResponseRedirect('/todo/')
