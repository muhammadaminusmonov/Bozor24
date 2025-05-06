from django.urls import path 
from .views import get_ctg_list, detail_ctg

urlpatterns = [
    path("", get_ctg_list, name="ctg_list" ),
    path("<int:pk>/", detail_ctg, name="ctg_details")
]