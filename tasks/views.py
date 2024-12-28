from django.shortcuts import render
from .models import Task, Tenant
# Create your views here.


def task_list(request):
    print("request.tenant   :", request.tenant)
    if not request.tenant:
        return render(request, 'error.html', {"message": "Tenant not found"})
    print("request.tenant   : ", request.tenant)
    task = Task.objects.filter(tenant=request.tenant)
    print("task    : ", task)
    return render(request, 'task_list.html', {"tasks": task, 'tenant': request.tenant})