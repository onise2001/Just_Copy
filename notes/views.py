from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.viewsets import ModelViewSet

class NoteList(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    