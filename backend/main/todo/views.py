from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo


def home_page(request):
    tasks = Todo.objects.order_by('-created')
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todotemps/home.html', context)


def update_page(request, pk):
    task = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=task)

    context = {'task': task, 'form': form}
    return render(request, 'todotemps/update.html', context)


def delete_page(request, pk):
    task = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}
    return render(request, 'todotemps/delete.html', context)   
