from django.urls import path
from .views import RegionListCreateView, RegionRetrieveUpdateDeleteView

urlpatterns = [
    path('', RegionListCreateView.as_view(), name='region-list-create'),      # GET, POST
    path('<int:pk>/', RegionRetrieveUpdateDeleteView.as_view(), name='region-detail'),  # GET, PUT, DELETE
]
