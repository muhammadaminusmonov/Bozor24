from django.urls import path 
from .views import get_ctg_list, detail_ctg, admin_ctg_post

urlpatterns = [
    path("", get_ctg_list, name="ctg_list" ),
    path("admin/", admin_ctg_post, name="ctg_post_admin"),
    path("<int:pk>/", detail_ctg, name="ctg_details")
]