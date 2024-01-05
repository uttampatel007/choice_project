from django.urls import path, include
from .views import choices

app_name = "choices"

urlpatterns = [
    path("", choices, name="choices"),
]
