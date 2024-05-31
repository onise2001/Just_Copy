from django.urls import path, include
from .views import NoteList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notes', NoteList)


urlpatterns = [
    path("", include(router.urls)),
]
