from django.urls import path
from .views import UserLoginTokenObtainPairView, UserLoginTokenRefreshView

urlpatterns = [
    path('', UserLoginTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', UserLoginTokenRefreshView.as_view(), name='token_refresh'),
]