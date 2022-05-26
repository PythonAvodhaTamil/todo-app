from django.shortcuts import redirect, render
from todo_app.models import ToDolist



def add_task (request):
    """
    This function get the text from form(add_task.html) 
    and
    saved it in our database ToDolist
    """
    if request.method=='POST':
        text=request.POST['text']
        s=ToDolist(text=text)
        s.save()
        # return redirect('')
    todo_list=ToDolist.objects.all()
    return render(request,"add_task.html",{'items': todo_list})

def task(request):
    """
    It read the data  from the database ToDolist 
    and 
    creating the tables (task.html)
    
    """
    todo_list=ToDolist.objects.all()
    return render(request,'task.html',{'items': todo_list})

def delete (request,id):
    """
    This function get the text from form(add_task.html) 
    and 
    delete it in our database ToDolist
    """
   
    s=ToDolist.objects.get(id=id)
    s.delete()
    return redirect('add_task')
    




