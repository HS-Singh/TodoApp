from rest_framework import viewsets
# Create your views here.

from .models import Todo
from .serializers import TodoSerializer

class TodoView(viewsets.ModelViewSet):
	serializer_class=TodoSerializer
	queryset=Todo.objects.all()