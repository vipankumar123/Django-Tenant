<!DOCTYPE html>
<html>
<head>
    <title>{{ tenant.name }}'s Tasks</title>
</head>
<body>
    <h1>Tasks for {{ tenant.name }}</h1>
    <ul>
        {% for task in tasks %}
            <li>
                <strong>{{ task.title }}</strong>: {{ task.description }}
                {% if task.completed %}
                    [Completed]
                {% else %}
                    [Pending]
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>




<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
</body>
</html>





# Create your models here.

from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.tenant.name}] {self.title}"





from tasks.models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        domain = request.META.get('HTTP_HOST', '').split(':')[0]
        try:
            request.tenant = Tenant.objects.get(domain=domain)
        except Tenant.DoesNotExist:
            request.tenant = None
        return self.get_response(request)