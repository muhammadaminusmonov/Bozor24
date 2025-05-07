from django.urls import path
from .views import LoginWithAccessTokenView, RefreshAccessTokenView

urlpatterns = [
    path('', LoginWithAccessTokenView.as_view(), name='login-with-token'),
    path('refresh/', RefreshAccessTokenView.as_view(), name='refresh-token'),
]
