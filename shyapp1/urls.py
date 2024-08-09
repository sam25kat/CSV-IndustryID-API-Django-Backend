from django.urls import path
from .views import UploadCSVView, IndustryIDKeyView

urlpatterns = [
    path('upload/', UploadCSVView.as_view(), name='upload'),
    path('industrycred/', IndustryIDKeyView.as_view(), name='industrycred'),
]
