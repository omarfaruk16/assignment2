from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView, ListView, UpdateView, DeleteView
from .models import TodoModel, FormModel
from .forms import TodoForm, FormNameForm
from django.shortcuts import redirect,render

class TodoCreateView(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')
  

def FormNameCreateView(request):
    if request.method == 'POST':
        form = FormNameForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("todo_create")
    else:
        form = FormNameForm()
    return render(request,'formname.html', {'form' : form})    

    
# class TodoListnameView(ListView):
#     model = FormModel
#     template_name = 'todo_list.html'
#     context_object_name = 'todoname'

def TodoListView(request):
    todos = TodoModel.objects.all()
    todoname = FormModel.objects.all()
    
    value = {
        'todos': todos,
        'todoname': todoname
    }
    
    return render(request,'todo_list.html', value)
    
class update_todo(UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')
    
class delete_todo(DeleteView):
    model = TodoModel
    template_name = 'delete_conform.html'
    success_url = reverse_lazy('todo_list')
    
def complete_todo(request,pk):
    std = TodoModel.objects.get(pk = pk).delete()
    return redirect('todo_list')
